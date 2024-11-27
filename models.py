from abc import ABC, abstractmethod


class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar * 0.8)  # Olcsóbb ár

    def jarat_tipus(self):
        return "Belföldi"


class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar * 1.2)  # Magasabb ár

    def jarat_tipus(self):
        return "Nemzetközi"


class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)


class JegyFoglalas:
    def __init__(self, jaratszam, utas_nev):
        self.jaratszam = jaratszam
        self.utas_nev = utas_nev

    def __str__(self):
        return f"Foglalás: {self.utas_nev} - Járat: {self.jaratszam}"
