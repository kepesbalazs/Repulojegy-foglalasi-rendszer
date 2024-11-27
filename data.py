from models import BelfoldiJarat, NemzetkoziJarat, LegiTarsasag, JegyFoglalas

legi_tarsasag = LegiTarsasag("Repülőkék")
legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B101", "Budapest", 10000))
legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B102", "Pécs", 8000))
legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N201", "Berlin", 50000))

foglalasok = [
    JegyFoglalas("B101", "Kiss Péter"),
    JegyFoglalas("B102", "Nagy Anna"),
    JegyFoglalas("N201", "Tóth Gábor"),
    JegyFoglalas("B101", "Szabó Márta"),
    JegyFoglalas("N201", "Varga László"),
    JegyFoglalas("B102", "Farkas Júlia"),
]
