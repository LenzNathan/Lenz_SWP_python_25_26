import random

# Generiert n eindeutige Zufallszahlen aus dem Bereich 1 bis out_of (inklusive)
def get_numbers(n=6, out_of=45, verbose=False):
    if n > out_of:
        raise ValueError("n must be less or equal to out_of")
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if out_of <= 0:
        raise ValueError("out_of must be greater than 0")
    numbers = []
    for i in range(out_of):
        numbers.append(i)
    for i in range(n):
        if verbose:
            print("Step", i, ":\t", numbers)
        r = random.randint(0, out_of - i - 1)
        numbers[r], numbers[out_of - i - 1] = numbers[out_of - i - 1], numbers[r]
    if verbose:
        print("Final  :\t", numbers)
    for i in range(out_of - n, out_of):
        numbers[i] += 1
    if verbose:
        print("Readable:\t", numbers)
    return numbers[out_of - n:out_of]

# Analysiert eine bestimmte Anzahl an Ziehungen und zählt, wie oft jede Zahl gezogen wurde
def analyze_numbers(amount, n=6, out_of=45):
    d = {}
    for i in range(amount):
        nums = get_numbers(n, out_of)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
    return d

# Berechnet und zeigt die Statistik der gezogenen Zahlen
def calc_and_show_stats(n=6, out_of=45, amount=100000):
    a = analyze_numbers(amount, n, out_of)
    total_amount = amount * n
    for i in sorted(a.keys()):
        print(a[i], "\t", i, " \t", round(a[i] / total_amount * 100, 2), "%")

# Benutzereingabe zum Experimentieren mit den Parametern und Starten der Analyse/n
def activate_ui():
    n = 6
    out_of = 45
    amount = 100000
    print(
        "Lottozahlen Generator - manipuliere mit 'n <Zahl>', 'out_of <Zahl>', 'amount <Zahl>' oder starte die Analyse mit 'analyze'")
    s = input().strip()
    while s != "exit":
        if s != "":
            try:
                if s.startswith("n"):
                    n = int(s.split(" ")[1])
                    print("n set to", n)
                elif s.startswith("out_of"):
                    out_of = int(s.split(" ")[1])
                    print("out_of set to", out_of)
                elif s.startswith("amount"):
                    amount = int(s.split(" ")[1])
                    print("amount set to", amount)
                elif s.startswith("analyze"):
                    print("Analyzing", amount, "draws with", n, "out of", out_of)
                    calc_and_show_stats(n, out_of, amount)
                elif s.startswith("generate -v"):
                    print("Ordered:\t", sorted(get_numbers(n, out_of, True)))
                elif s.startswith("generate"):
                    print(sorted(get_numbers(n, out_of)))
                else:
                    print("Unknown command")
            except IndexError as e:
                print("invalid syntax")
            except ValueError as e:
                print("the settings were set to an invalid Value:", e)
        s = input().strip()

# Hauptmethode
def main():
    activate_ui()

# Programmstart
if __name__ == "__main__":
    main()

# 1. eine Main methode (Code wird beim Einbinden noch nicht ausgeführt)
# 2. Englische Sprache, snake case
# 3. Funktionen beschreiben (1 Zeile)
# 4. Keine Variablen hard coded lassen (Anpassbarkeit, globale Variablen vermeiden, Code soll nicht mehr verändert werden müssen)
# 5. Methoden atomar machen (Sortieren nicht in get_numbers)


# gewählte Zahl an die letzte Stelle schieben, letzte Zahl an die gewählte Stelle schieben, Zufalls range verkleinern
