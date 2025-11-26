{\rtf1\ansi\ansicpg1250\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from datetime import datetime\
\
class SavingsManager:\
    def __init__(self, database):\
        self.db = database       # adatb\'e1zis objektum\
        self.felretett = 0       # f\'e9lretett p\'e9nz\
        self.aktualis = 0        # aktu\'e1lis egyenleg\
\
    # -------------------------------------------------------\
    def beallit_felretett(self, osszeg):\
        """\
        Be\'e1ll\'edtja a f\'e9lretett \'f6sszeget \'e9s elmenti adatb\'e1zisba.\
        """\
        self.felretett = osszeg\
        self.db.save_savings(osszeg)\
        return True\
\
    # -------------------------------------------------------\
    def ellenoriz_keret(self):\
        """\
        Ellen\uc0\u337 rzi, hogy az aktu\'e1lis egyenleg kisebb-e a f\'e9lretett \'f6sszegn\'e9l.\
        Ha igen, figyelmeztet\uc0\u337  jelz\'e9st ad.\
        """\
        if self.aktualis < self.felretett:\
            return self.jelzes_uzenet(\
                "T\'fall\'e9pted a f\'e9lretett p\'e9nzt!", \
                tipus="figyelmeztet\'e9s"\
            )\
        else:\
            return self.jelzes_uzenet(\
                "Minden rendben, a kereten bel\'fcl vagy.",\
                tipus="ok"\
            )\
\
    # -------------------------------------------------------\
    def jelzes_uzenet(self, szoveg, tipus):\
        """\
        Kezeli a vizu\'e1lis jelz\'e9seket.\
        tipus:\
            - 'figyelmeztet\'e9s' \uc0\u8594  piros \'fczenet\
            - 'ok' \uc0\u8594  z\'f6ld \'fczenet\
        """\
        return \{\
            "uzenet": szoveg,\
            "tipus": tipus,\
            "szin": "piros" if tipus == "figyelmeztet\'e9s" else "z\'f6ld",\
            "idopont": datetime.now()\
        \}\
\
    # -------------------------------------------------------\
    def frissit_egyenleg(self, uj_egyenleg):\
        """\
        Friss\'edti az aktu\'e1lis egyenleget \'e9s ellen\uc0\u337 rzi, hogy t\'fall\'e9p\'e9s t\'f6rt\'e9nt-e.\
        """\
        self.aktualis = uj_egyenleg\
        return self.ellenoriz_keret()\
\
    # -------------------------------------------------------\
    def ment_felretett(self):\
        """\
        A 'Ment\'e9s' gomb m\uc0\u369 k\'f6d\'e9se:\
        elmenti a f\'e9lretett \'f6sszeget az adatb\'e1zisba.\
        """\
        self.db.save_savings(self.felretett)\
        return self.jelzes_uzenet(\
            "F\'e9lretett \'f6sszeg sikeresen mentve.",\
            tipus="ok"\
        )\
}