names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

# Erzeuge aus diesen Listen eine gefilterte Liste von Personen, die folgende Bedingungen erfüllt:
# ≥ 18 und Score ≥ 80
# müssen verwendet werden:
# zip – kombiniere die drei Listen so, dass jeder Eintrag ein Tupel (name, age, score) ist.
# filter + lambda – filtere alle Personen heraus, die beide Bedingungen erfüllen.
# map + lambda – forme jedes Tupel in ein Dictionary der Form
# {"name": ..., "age": ..., "score": ...} um.
# {"name": "Anna", "age": 23, "score": 88}

zip_it = zip(names, ages, scores)
zipped = list(zip_it)
print(zipped)

filtered = filter(lambda x: x[1] >= 18 and x[2] >= 80, zipped)
# print(list(filtered)) #muss auskommentiert bleiben, da sonst der Filter schon durchgeloopt wird - nur zum Testen

dicts = map(lambda x: {"name": x[0], "age": x[1], "score": x[2]}, filtered)
result = list(dicts)
print(result)

# und nochmal in einer Zeile:
print(list(map(lambda x: {"name": x[0], "age": x[1], "score": x[2]},
               filter(lambda x: x[1] >= 18 and x[2] >= 80, zip(names, ages, scores)))))
