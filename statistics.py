from typing import List, Tuple
from math import sqrt
from db_manager import Trans, trans_has_cat, cat
from sqlalchemy import func


#Összes költség

def total_expense(transactions: List[Trans]) -> float:
    return float(sum(t.money for t in transactions if t.money < 0))

#Kategóriánkénti összesített kiadás
def total_by_category(session) -> List[Tuple[str, float]]:

    results = (
        session.query(cat.name, func.sum(Trans.money))
        .join(trans_has_cat, cat.id == trans_has_cat.c.id_cat)
        .join(Trans, Trans.id == trans_has_cat.c.id_trans)
        .filter(Trans.money < 0)
        .group_by(cat.name)
        .all()
    )
    '''
    [
    ("Étel", -825.0),
    ("Közlekedés", -180.0),
    ]
    '''

    return [(name, float(total or 0)) for name, total in results]


#Havi kiadások napokra lebontva
def monthly_expenses(session, year: int, month: int) -> List[Tuple[int, float]]:

    rows = (
        session.query(
            func.strftime("%d", Trans.date).label("day"),
            func.sum(Trans.money).label("total")
        )
        .filter(func.strftime("%Y", Trans.date) == str(year))
        .filter(func.strftime("%m", Trans.date) == f"{month:02d}")
        .filter(Trans.money < 0)
        .group_by("day")
        .all()
    )

    return [(int(day), float(total)) for day, total in rows]


def average_expense(transactions: List[Trans]) -> Tuple[float, float]:

    expenses = [t.money for t in transactions if t.money < 0]
    if not expenses:
        return 0.0, 0.0

    total = sum(expenses)
    dates = [t.date for t in transactions]
    days = (max(dates) - min(dates)).days + 1 #hány nap telt el

    #időtartam szerint
    weeks = days / 7
    months = days / 30.437 

    weekly_avg = total / weeks if weeks > 0 else total
    monthly_avg = total / months if months > 0 else total

    return float(weekly_avg), float(monthly_avg)



def std_expense(transactions: List[Trans]) -> float:

    values = [t.money for t in transactions if t.money < 0]

    if len(values) < 2:
        return 0.0

    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)

    return float(sqrt(variance))
