# - Magic methods
#
# - len(a) = a.__len__()
#
# - Auto Klasse erzeugen
# - PS als attribut vergeben
# - wenn a1 50PS hat und a2 60PS und a1+a2 rechnet soll direkt 110 ausgegeben werden
# - subtraktion und multiplikation soll auf den auto-objekten möglich sein
# - achtung überprüfen ob geegnete objekte addiert, subtrahiert usw. werden
# - EQ,LT,GT vergleichsoperationen abbilden
# - für alle magicmethods testzeilen angeben
#
#
#
# später bei linkedlist:
#
#  __setitem__ __getitem__ __contains__=in operator
#
# with = contextmanager klappt, wenn eine klasse __enter_ und __exit implementiert
#
# iteratoren müssen __iter__ __next__ implementiert next braucht raise Stopiteration

class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        return TypeError

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        return TypeError

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        return TypeError

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return TypeError

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return TypeError

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return TypeError

if __name__ == "__main__":
    a1 = Auto(5)
    a2 = Auto(6)

    print("Addition:", a1 + a2)  # 11
    print("Subtraktion:", a2 - a1)  # 1
    print("Multiplikation:", a1 * a2)  # 30
    print("Gleichheit:", a1 == a2)  # False
    print("Kleiner als:", a1 < a2)  # True
    print("Größer als:", a1 > a2)  # False