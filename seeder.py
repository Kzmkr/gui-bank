from datetime import date
from db_manager import TransactionManager, cat

def seed_database():
    """Adatbázis feltöltése példa adatokkal."""
    manager = TransactionManager()
    
    if manager.get_all_trans():
        print("Az adatbázis már tartalmaz adatokat. Feltöltés kihagyva.")
        return

    print("Adatbázis feltöltése...")

    income = cat(name="Bevétel")
    work = cat(name="Munka")
    food = cat(name="Étel")
    transport = cat(name="Közlekedés")
    entertainment = cat(name="Szórakozás")
    utilities = cat(name="Rezsi")
    shopping = cat(name="Vásárlás")
    health = cat(name="Egészség")
    education = cat(name="Oktatás")
    gifts = cat(name="Ajándékok")
    subscriptions = cat(name="Előfizetések")
    insurance = cat(name="Biztosítás")
    savings = cat(name="Megtakarítások")
    investments = cat(name="Befektetések")
    
    manager.session.add_all([
        income, work, food, transport, entertainment, utilities, shopping,
        health, education, gifts, subscriptions, insurance, savings, investments
    ])
    manager.session.commit()
    
    manager.add_trans(3500, "Havi fizetés", date(2025, 10, 1), [income, work])
    manager.add_trans(-1200, "Albérlet", date(2025, 10, 1), [utilities])
    manager.add_trans(-250, "Bevásárlás", date(2025, 10, 2), [food])
    manager.add_trans(-60, "Benzinkút", date(2025, 10, 2), [transport])
    manager.add_trans(-45, "Gyógyszertár", date(2025, 10, 3), [health])
    manager.add_trans(-15, "Netflix", date(2025, 10, 3), [subscriptions, entertainment])
    manager.add_trans(-80, "Vacsora randi", date(2025, 10, 4), [food, entertainment])
    manager.add_trans(200, "Bónusz", date(2025, 10, 5), [income, work])
    manager.add_trans(-120, "Új cipő", date(2025, 10, 5), [shopping])
    manager.add_trans(-35, "Mozi jegyek", date(2025, 10, 6), [entertainment])
    manager.add_trans(-500, "Átutalás megtakarításba", date(2025, 10, 7), [savings])
    manager.add_trans(-95, "Internet számla", date(2025, 10, 7), [utilities])
    manager.add_trans(-180, "Bevásárlás", date(2025, 10, 8), [food])
    manager.add_trans(-50, "Születésnapi ajándék", date(2025, 10, 9), [gifts, shopping])
    manager.add_trans(800, "Szabadúszó projekt", date(2025, 10, 9), [income, work])
    manager.add_trans(-25, "Uber", date(2025, 10, 10), [transport])
    manager.add_trans(-150, "Orvosi vizit", date(2025, 10, 10), [health])
    manager.add_trans(-12, "Spotify", date(2025, 10, 11), [subscriptions, entertainment])
    manager.add_trans(-220, "Villanyszámla", date(2025, 10, 11), [utilities])
    manager.add_trans(-65, "Éttermi ebéd", date(2025, 10, 12), [food])
    manager.add_trans(-200, "Online kurzus", date(2025, 10, 13), [education])
    manager.add_trans(-90, "Bevásárlás", date(2025, 10, 13), [food])
    manager.add_trans(-300, "Autóbiztosítás", date(2025, 10, 14), [insurance, transport])
    manager.add_trans(-75, "Könyvek", date(2025, 10, 14), [education, shopping])
    manager.add_trans(-40, "Kávézó", date(2025, 10, 15), [food, entertainment])
    manager.add_trans(-1000, "Befektetés részvényekbe", date(2025, 10, 15), [investments, savings])
    manager.add_trans(-55, "Benzinkút", date(2025, 10, 16), [transport])
    manager.add_trans(3500, "Havi fizetés", date(2025, 9, 1), [income, work])
    manager.add_trans(-1200, "Albérlet", date(2025, 9, 1), [utilities])
    manager.add_trans(-230, "Bevásárlás", date(2025, 9, 5), [food])
    manager.add_trans(-450, "Új telefon", date(2025, 9, 10), [shopping])
    manager.add_trans(500, "Szabadúszó munka", date(2025, 9, 15), [income, work])
    manager.add_trans(-180, "Bevásárlás", date(2025, 9, 20), [food])
    manager.add_trans(-100, "Edzőterem tagság", date(2025, 9, 25), [health, subscriptions])
    manager.add_trans(3500, "Havi fizetés", date(2025, 8, 1), [income, work])
    manager.add_trans(-1200, "Albérlet", date(2025, 8, 1), [utilities])
    manager.add_trans(-800, "Nyaralási költségek", date(2025, 8, 10), [entertainment, food])
    manager.add_trans(-250, "Bevásárlás", date(2025, 8, 15), [food])
    manager.add_trans(300, "Régi laptop eladása", date(2025, 8, 20), [income])
    manager.add_trans(-200, "Bevásárlás", date(2025, 8, 25), [food])
    
    print("Adatbázis feltöltve példa adatokkal.")

if __name__ == "__main__":
    seed_database()
