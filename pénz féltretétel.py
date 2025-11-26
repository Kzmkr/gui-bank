from datetime import datetime

class SavingsManager:
    def __init__(self, database):
        self.db = database
        self.felretett = 0
        self.aktualis = 0

    def beallit_felretett(self, osszeg):
        self.felretett = osszeg
        self.db.save_savings(osszeg)
        return True

    def ellenoriz_keret(self):
        if self.aktualis < self.felretett:
            return self.jelzes_uzenet("Túllépted a félretett pénzt!", "figyelmeztetés")
        else:
            return self.jelzes_uzenet("Minden rendben, a kereten belül vagy.", "ok")

    def jelzes_uzenet(self, szoveg, tipus):
        return {
            "uzenet": szoveg,
            "tipus": tipus,
            "szin": "piros" if tipus == "figyelmeztetés" else "zöld",
            "idopont": datetime.now()
        }

    def frissit_egyenleg(self, uj_egyenleg):
        self.aktualis = uj_egyenleg
        return self.ellenoriz_keret()

    def ment_felretett(self):
        self.db.save_savings(self.felretett)
        return self.jelzes_uzenet("Félretett összeg sikeresen mentve.", "ok")
