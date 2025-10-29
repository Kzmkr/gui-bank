from db_manager import TransactionManager
from datetime import date

tm = TransactionManager()  


food_cat = tm.get_all_cat()[0] 
tm.add_trans(-50, "Nasi", date.today(), [food_cat])


for t in tm.get_all_trans():
    print(f"{t.from_to}: {t.money} - {t.date}")
    for c in t.categories:
        print(f"    {c.name}")


print("\nKategóriák:")
for c in tm.get_all_cat():
    print(f"  {c.name}")


# Példa: Új kategória hozzáadása
new_category = tm.add_cat("Rezsi")
print(f"Hozzáadott kategória: {new_category.name}")

# Példa: Kategória hozzáadása egy tranzakcióhoz
transaction = tm.get_all_trans()[0]  # Feltételezve, hogy van legalább egy tranzakció
tm.add_cat_to_trans(transaction, new_category)
print(f"Hozzáadott kategória '{new_category.name}' a(z) '{transaction.from_to}' tranzakcióhoz")

# Példa: Kategória eltávolítása egy tranzakcióból
tm.remove_cat_from_trans(transaction, new_category)
print(f"Eltávolított kategória '{new_category.name}' a(z) '{transaction.from_to}' tranzakcióból")

# Példa: Kategória átnevezése
tm.rename_cat(new_category, "Számlák")
print(f"Kategória átnevezve: {new_category.name}")

# Példa: Tranzakció szerkesztése
tm.edit_trans(transaction, -100, "Vacsora", date.today(), [new_category])
print(f"Szerkesztett tranzakció: {transaction.from_to}, {transaction.money}, {transaction.date}")

# Példa: Kategória törlése
tm.del_cat(new_category)
print("Kategória törölve: 'Számlák'")

# Példa: Tranzakció törlése
tm.del_trans(transaction)
print("Tranzakció törölve")
