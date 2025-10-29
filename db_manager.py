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
        return self.session.query(Trans).all()

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
