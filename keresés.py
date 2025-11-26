from datetime import date

def search_transactions(
    tm,
    kategoria=None,
    datum_tol=None,
    datum_ig=None,
    osszeg_min=None,
    osszeg_max=None,
    leiras=None
):
    """Visszaadja azokat a tranzakciókat, amelyek megfelelnek a megadott szűrőknek."""

    results = []

    for t in tm.get_all_trans():
        
        # --- Kategória szűrés ---
        if kategoria:
            # Ha egy kategóriát adtunk meg
            if not isinstance(kategoria, list):
                kategoria = [kategoria]

            # Ellenőrizzük, hogy t.categories tartalmazza-e a keresett kategóriákat
            if not any(cat in t.categories for cat in kategoria):
                continue

        # --- Dátum szűrés ---
        if datum_tol and t.date < datum_tol:
            continue
        if datum_ig and t.date > datum_ig:
            continue

        # --- Összeg tartomány szűrés ---
        if osszeg_min is not None and t.money < osszeg_min:
            continue
        if osszeg_max is not None and t.money > osszeg_max:
            continue

        # --- Leírás szűrés ---
        if leiras and leiras.lower() not in t.from_to.lower():
            continue

        results.append(t)

    return results
