import string


# alle arten von list comprehensions
# einmal mit if, ifelse, und einmal ohne
# für dicts, sets und lists
# beispiele überlegen

# Does some list comprehensions and prints the results for practice
def check_lcs():
    # Quadratische funktion -5 bis 5
    print("Square function from -5 to 5")

    d = {x: x * x for x in range(-5, 6)}
    print(d)
    l = [x * x for x in range(-5, 6)]
    print(l)
    s = {x * x for x in range(-5, 6)}
    print(s)

    # 3n+1 (if-else)
    print("\n3n+1 for the first 10 numbers")

    d = {x: 3 * x + 1 if x % 2 != 0 else x / 2 for x in range(1, 11)}
    print(d)
    l = [3 * x + 1 if x % 2 != 0 else x / 2 for x in range(1, 11)]
    print(l)
    s = {3 * x + 1 if x % 2 != 0 else x / 2 for x in range(1, 11)}
    print(s)

    # gerade Zahlen
    print("\nEven numbers from 1 to 20")
    d = {x: x for x in range(1, 21) if x % 2 == 0}
    print(d)
    l = [x for x in range(1, 21) if x % 2 == 0]
    print(l)
    s = {x for x in range(1, 21) if x % 2 == 0}
    print(s)


def alphabet_dict():
    print("\nAlphabet dictionary:")
    letters = string.ascii_lowercase + string.ascii_uppercase
    # enumerate erstellt für alles einen index
    letter_dict = {letter: index + 1 for index, letter in enumerate(letters)}
    print(letter_dict)
    return letter_dict
    # chr(n) schaut in der ascii tabelle nach und findet das richtige char
    # tuple sind immutable also unveränderlich, wenn man nur Daten Speichern will, kann man sie verwenden
    # sind gegen Änderungen geschützt
    # Iterable ist eine Datenstruktur, die einen Startwert hat und weiß wie das nächste Element zu errechnen ist
    # dabei brauchen wir keine Zählvariable (speicherschonend)
    #


def main():
    check_lcs()
    alphabet_dict()


if __name__ == "__main__":
    main()
    alphabet_dict()

# mit list comprehensions die Funktionalität einer Set abbilden (dict/list -> set)
# dict comprehension mit ergebnis: schlüssel sind die chars, 0-anzah der chars
# {'a':1, 'b':2, ..., evtl. 'A':27, 'B':28, ...}

# immutable (nicht veränderbar): sie können an der Speicherstelle nichtmehr verändert werden - wenn
# sie codemäßig verändert werden, dann wird ein neuer Speicherplatz beschrieben und die Referenz aktualisiert

# primitive Datentypen: immutable
# listen: mutable
# String: immutable
# rest nachschauen (link in den Folien)

# Seiteneffekt: globale Variablen werden von Methoden verändert, andere Methoden können durch diese Änderungen
# beeinflusst werden / crashen

# funktionale programmierung: die gesamte Information wird durch Parameter übergeben, keine globalen Variablen
# notwendig


rset = {"apple", "banana", "cherry", "date", "apple", "elderberry", "fig", "cherry"}
rset.add("banana") # Veränderbar
rtuple = ("apple", "banana", "cherry", "date", "apple", "elderberry", "fig", "cherry") #unveränderbar
rlist = ["apple", "banana", "cherry", "date", "apple", "elderberry", "fig", "cherry"] # Veränderbar
rlist.append("banana")
print(rset)
print(rtuple)
print(rlist)

