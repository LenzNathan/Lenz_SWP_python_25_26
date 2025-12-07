# Gegeben:
# Liste von Temperaturen in °C
# Anforderungen:
# Funktion, filtert Fehlwerte heraus (extremer als -60 und 60 °C)
# gibt bereinigte Liste zurück und die Anzahl der Fehlwerte
# Funktion berechnet die Durchschnittstemperatur einer Datenreihe
# so gestalten, dass sie auch mit leeren Listen umgehen können
# BSP: main füht das ganze mit sinnvollem zeug aus
import sys


def between(lower, higher, elements):
    outer_elements = [] #indices of outliers
    for e in elements:
        i = elements.index(e)
        if type(e) == str:
            try:
                elements[i] = float(e.replace(",", "."))
                e = elements[i]
            except:
                outer_elements.append(i)
                continue
        if type(e) != float and type(e) != int:
            outer_elements.append(i)
            continue
        if e < lower or e > higher:
            outer_elements.append(i)

    for i in range(len(outer_elements)):
        elements[i], elements[outer_elements[i]] = elements[outer_elements[i]], elements[i]
    return elements[len(outer_elements):], len(outer_elements)


def average(elements):
    if len(elements) == 0:
        return "No data"
    return sum(elements) / len(elements)


def main():
    try:
        temps = [22.5, 25.0, -70.0, 19.5, 60.5, 18.0, 21.0, -65.0, 23.0]
        cleaned_temps, error_count = between(-60, 60, temps)
        avg = average(cleaned_temps)
        temps = []
        cleaned_temps, error_count = between(-60, 60, temps)
        avg = average(cleaned_temps)
        temps = ["can u handle this?"]
        cleaned_temps, error_count = between(-60, 60, temps)
        avg = average(cleaned_temps)
        temps = [22.5, 25.0, -70.0, 19.5, 60.5, 18.0, 21.0, -65.0, 23.0, "what about that?", 15.0]
        cleaned_temps, error_count = between(-60, 60, temps)
        avg = average(cleaned_temps)
        temps = ["1.2", "3","120"]
        print("Original temperatures:", temps)
        cleaned_temps, error_count = between(-60, 60, temps)
        print("Cleaned temperatures:", cleaned_temps)
        print("Number of removed values:", error_count)
        avg = average(cleaned_temps)
        print("Average temperature:", avg)
    except Exception as e:
        print("A terrible error occurred: " + str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
