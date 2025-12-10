from datetime import date
from sqlalchemy import (
    create_engine, Column, Integer, Float, String, Date, ForeignKey, Table
)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# ---- Alap és Motor ----
Base = declarative_base()
engine = create_engine("sqlite:///data.db", echo=False)
Session = sessionmaker(bind=engine)

# ---- Many-to-many tábla ----
trans_has_cat = Table(
    "trans_has_cat",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("id_cat", Integer, ForeignKey("cat.id")),
    Column("id_trans", Integer, ForeignKey("trans.id")),
)

# ---- Modellek ----
class Trans(Base):
    __tablename__ = "trans"
    id = Column(Integer, primary_key=True)
    money = Column(Float, nullable=False)
    from_to = Column(String, nullable=False)
    date = Column(Date, nullable=False)

    categories = relationship(
        "cat",
        secondary=trans_has_cat,
        back_populates="transactions"
    )

class cat(Base):
    __tablename__ = "cat"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    transactions = relationship(
        "Trans",
        secondary=trans_has_cat,
        back_populates="categories"
    )

class RecurringTrans(Base):
    __tablename__ = "recurring_trans"
    id = Column(Integer, primary_key=True)
    money = Column(Float, nullable=False)
    from_to = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    category_id = Column(Integer, ForeignKey("cat.id"), nullable=False)
    
    category = relationship("cat")

class Savings(Base):
    __tablename__ = "savings"
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    category_id = Column(Integer, ForeignKey("cat.id"), nullable=True)

    category = relationship("cat")

# ---- Táblák létrehozása ----
Base.metadata.create_all(engine)

# ---- Tranzakciókezelő ----
class TransactionManager:
    def __init__(self):
        # Create session internally
        self.session = Session()

    # ---- Tranzakciók ----
    def add_trans(self, money: float, from_to: str, date_: date, categories: list):
        """
        Tranzakció hozzáadása kategóriákkal.
        Kategóriák: cat objektumok listája
        """
        trans = Trans(money=money, from_to=from_to, date=date_)
        
        for category in categories:
            if not isinstance(category, cat):
                raise ValueError(f"A kategóriának cat objektumnak kell lennie, de {type(category)} típust kapott.")
        
        trans.categories.extend(categories)
        self.session.add(trans)
        self.session.commit()
        print(f"Tranzakció hozzáadva: {trans.from_to}, {trans.money}, {trans.date}")
        return trans

    def get_all_trans(self):
        """
        Get all transactions including one-time and generated from recurring.
        Returns: List of Trans objects
        """
        from datetime import date as date_module
        
        # Get all one-time transactions
        all_trans = self.session.query(Trans).all()
        
        # Get all recurring transactions and generate Trans objects for each month
        recurring_trans = self.session.query(RecurringTrans).all()
        today = date_module.today()
        
        for recurring in recurring_trans:
            current_date = recurring.start_date
            
            # Generate monthly transactions from start_date to today
            while current_date <= today:
                # Create a virtual Trans object (not saved to DB)
                virtual_trans = Trans(
                    money=recurring.money,
                    from_to=recurring.from_to,
                    date=current_date
                )
                # Set the category
                virtual_trans.categories = [recurring.category]
                all_trans.append(virtual_trans)
                
                # Add one month
                if current_date.month == 12:
                    try:
                        current_date = current_date.replace(year=current_date.year + 1, month=1)
                    except ValueError:
                        current_date = current_date.replace(year=current_date.year + 1, month=2, day=28)
                else:
                    try:
                        current_date = current_date.replace(month=current_date.month + 1)
                    except ValueError:
                        next_month = current_date.month + 1
                        if next_month == 2:
                            current_date = current_date.replace(month=next_month, day=28)
                        elif next_month in [4, 6, 9, 11]:
                            current_date = current_date.replace(month=next_month, day=30)
                        else:
                            current_date = current_date.replace(month=next_month, day=31)
        
        return all_trans

    # ---- Kategóriák ----
    def add_cat(self, name: str):
        """
        Új kategória hozzáadása, ha még nem létezik.
        Visszatér: cat objektum
        """
        existing_cat = self.session.query(cat).filter_by(name=name).first()
        if existing_cat:
            print(f"A(z) '{name}' kategória már létezik.")
            return existing_cat

        new_cat = cat(name=name)
        self.session.add(new_cat)
        try:
            self.session.commit()
            print(f"Új kategória hozzáadva: {new_cat.name}")
        except Exception as e:
            self.session.rollback()
            print(f"Hiba történt a(z) '{name}' kategória hozzáadása során: {e}")
            raise e
        return new_cat

    def add_cat_to_trans(self, trans: Trans, category: cat):
        """
        Kategória hozzáadása egy tranzakcióhoz.
        """
        if category not in trans.categories:
            trans.categories.append(category)
            self.session.commit()

    def remove_cat_from_trans(self, trans: Trans, category: cat):
        """
        Kategória eltávolítása egy tranzakcióból.
        """
        if category in trans.categories:
            trans.categories.remove(category)
            self.session.commit()

    def del_cat(self, category: cat):
        """
        Kategória törlése.
        """
        self.session.delete(category)
        self.session.commit()
        print(f"Kategória törölve: {category.name}")

    def del_trans(self, trans: Trans):
        """
        Tranzakció törlése.
        """
        self.session.delete(trans)
        self.session.commit()
        print(f"Tranzakció törölve: {trans.from_to}, {trans.money}, {trans.date}")

    def rename_cat(self, category: cat, new_name: str):
        """
        Kategória átnevezése.
        """
        old_name = category.name
        category.name = new_name
        self.session.commit()
        print(f"Kategória átnevezve: {old_name} -> {new_name}")

    def edit_trans(self, trans: Trans, amount: float, partner: str, date_: date, categories: list):
        """
        Tranzakció részleteinek szerkesztése.
        """
        trans.money = amount
        trans.from_to = partner
        trans.date = date_
        trans.categories = categories
        self.session.commit()
        print(f"Tranzakció szerkesztve: {trans.from_to}, {trans.money}, {trans.date}")

    def get_all_cat(self):
        """
        Retrieve all categories.
        Returns: List of cat objects
        """
        return self.session.query(cat).all()

    # ---- Rendszeres tranzakciók ----
    def add_recurring_trans(self, money: float, from_to: str, start_date: date, category: cat):
        """
        Rendszeres tranzakció hozzáadása.
        """
        recurring = RecurringTrans(
            money=money,
            from_to=from_to,
            start_date=start_date,
            category_id=category.id
        )
        self.session.add(recurring)
        self.session.commit()
        print(f"Rendszeres tranzakció hozzáadva: {recurring.from_to}, {recurring.money}")
        return recurring

    def get_all_recurring_trans(self):
        """
        Összes rendszeres tranzakció lekérése.
        """
        return self.session.query(RecurringTrans).all()

    # ---- Félretett pénz (savings) ----
    def save_savings(self, amount: float, category: 'cat' = None, date_: date = None):
        """
        Ment egy félretett összeget az adatbázisba.
        Ha nincs megadva dátum, a mai dátumot használja.
        Visszatér: Savings objektum
        """
        from datetime import date as date_module
        if date_ is None:
            date_ = date_module.today()

        saving = Savings(amount=amount, date=date_)
        if category is not None:
            # accept either cat object or category name
            if isinstance(category, cat):
                saving.category_id = category.id
            elif isinstance(category, str):
                existing = self.session.query(cat).filter_by(name=category).first()
                if existing:
                    saving.category_id = existing.id
                else:
                    # create new category if it doesn't exist
                    newc = cat(name=category)
                    self.session.add(newc)
                    self.session.commit()
                    saving.category_id = newc.id
        self.session.add(saving)
        self.session.commit()
        print(f"Félretett összeg mentve: {saving.amount} Ft, {saving.date} ({saving.category.name if saving.category else 'no-cat'})")
        return saving

    def get_all_savings(self):
        """Visszaadja az összes félretett tételt (Savings objektumok listája)."""
        return self.session.query(Savings).order_by(Savings.date.desc()).all()

    def del_savings(self, saving: Savings):
        """Törli a megadott Savings bejegyzést."""
        self.session.delete(saving)
        self.session.commit()
        print(f"Félretett tétel törölve: {saving.amount} Ft, {saving.date}")

    def get_savings_as_list(self):
        """Segédfüggvény: (id, display_string) lista GUI-hoz."""
        savings = self.get_all_savings()
        return [(s.id, f"{s.date} - {s.amount:,.0f} Ft ({s.category.name if s.category else '-'})") for s in savings]

    def del_recurring_trans(self, recurring: RecurringTrans):
        """
        Rendszeres tranzakció törlése.
        """
        self.session.delete(recurring)
        self.session.commit()
        print(f"Rendszeres tranzakció törölve: {recurring.from_to}")

    def get_recurring_trans_as_list(self):
        """
        Rendszeres tranzakciók listája megjelenítéshez.
        Returns: List of tuples (id, display_string)
        """
        recurring_trans = self.get_all_recurring_trans()
        return [(rt.id, f"{rt.from_to} - {rt.money:,.0f} Ft ({rt.category.name})") 
                for rt in recurring_trans]
