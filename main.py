from data import legi_tarsasag, foglalasok
from models import JegyFoglalas


def jegy_foglalasa():
    print("\nElérhető járatok:")
    for jarat in legi_tarsasag.jaratok:
        print(f"{jarat.jaratszam}: {jarat.celallomas} ({jarat.jarat_tipus()}, Ár: {jarat.jegyar} Ft)")

    jaratszam = input("Adja meg a járatszámot: ")
    utas_nev = input("Adja meg az utas nevét: ")

    if any(jarat.jaratszam == jaratszam for jarat in legi_tarsasag.jaratok):
        foglalasok.append(JegyFoglalas(jaratszam, utas_nev))
        print("Foglalás sikeres!")
    else:
        print("Hibás járatszám!")


def foglalas_lemondasa():
    utas_nev = input("Adja meg az utas nevét: ")
    talalat = next((foglalas for foglalas in foglalasok if foglalas.utas_nev == utas_nev), None)

    if talalat:
        foglalasok.remove(talalat)
        print("Foglalás sikeresen lemondva!")
    else:
        print("Nem található ilyen foglalás.")


def foglalasok_listazasa():
    if foglalasok:
        print("\nAktuális foglalások:")
        for foglalas in foglalasok:
            print(foglalas)
    else:
        print("Nincsenek aktív foglalások.")


def menu():
    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Választás: ")

        if valasztas == "1":
            jegy_foglalasa()
        elif valasztas == "2":
            foglalas_lemondasa()
        elif valasztas == "3":
            foglalasok_listazasa()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")


if __name__ == "__main__":
    menu()
