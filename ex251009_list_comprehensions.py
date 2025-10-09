# alle arten von list comprehensions
# einmal mit if, ifelse, und einmal ohne
# für dicts, sets und lists
# beispiele überlegen
from statsmodels.tools.sequences import primes_from_2_to

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


def main():
    check_lcs()


if __name__ == "__main__":
    main()
