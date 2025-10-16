# Bankos # 

**Nyelv:** Python

**Felület:** qt

## Bankos - Feladatok és felelősök

| Funkció | Felelős |
|---|---|
| Kiadás, bevétel, pénz számontartás, kezdőoldal UI | Molnár Csegő |
| Befektetések | Dajka Bence IMI |
| Alap statisztikai adatok | Vaskó Dániel |
| Kategóriákhoz lehessen adni: kaja, elektronika | Kiss Péter |
| Rendszeres kiadás/bevétel | Botos Etele |
| Keresés filterek szerint | Varga Gábor |
| Pénz félretétele, jelez ha túllépted | Mázsári Patrik |
| Adatok kezelése, háttérbe | Kozma Kristóf |


## Adat kezelés ##

sqlite


python funckciók:

```python
	add_trans(amount:float, partner:str, date:date, cats:list):
		Returns: Trans object

	get_all_trans()
		Returns: List[Trans objects]

	add_cat(name:str)
		Returns: Trans object

	get_all_cat()
		Returns: List[Kat objects]

	add_cat_to_trans(trans,cat)
```

