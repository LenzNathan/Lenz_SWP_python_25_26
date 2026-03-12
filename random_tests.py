def dosomething(p1, p2, *g, **ge): # args und kwargs, g ist ein tuple, ge ein dict
    print(locals())

#Zuordnung der Parameter anhand von * und ** macht andere Namen möglich

dosomething(1,*(2, 3, 4, 5))
# Parameter werden von Agrs auf die definierten Parameter zugeordnet
dosomething(1, 2, 3, 4, 5, a=6, b=7)
# weitere Parameter verschwinden in args
# named variables (namen angeben) verschwinden in kwargs -> dict
# named parameter müssen nach den positional parameters kommen

# falls kein args da ist und zu viele Datentypen da sind, gibt es einen too many positional arguments
# die Reihenfolge muss gleich bleiben:
    # positional parameters
    # named parameters
    # *args
    # **kwargs
# und es muss definiert sein, dass wir es verwenden dürfen - wenn es kein args gibt, können wir es nicht verwenden um
# positional parameters zu definieren

def test(a,b,/,*,c): # alles rechts von /,* muss named angegeben werden
    print(a,b,c)



# Innere Funktionen:
    # Werden erst DEFINIERT und in den Speicher geschrieben, sobald die parent func aufgerufen wird

# Decorators:
    # @decorator -> interpretor wendet den decorator auf die func an und überschreibt die func mit dem Ergebnis
    # falls die func parameter hat, muss die wrapper func *args und **kwargs haben und an die func weitergeben

## Musterbeispiel für Decorator:
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # Before
#         value = func(*args, **kwargs)
#         # After
#         return value
#     return wrapper
