import random


def get_numbers():
    selectable_numbers = []
    for n in range(44):
        selectable_numbers.append(n + 1)
    lotto_numbers = []
    while len(lotto_numbers) < 6:
        n = random.choice(selectable_numbers)
        lotto_numbers.append(n)
        selectable_numbers.remove(n)
    lotto_numbers.sort()
    return lotto_numbers


def get_multiple_numbers(count):
    l_dict = {}
    for i in range(count):
        l_dict[i] = get_numbers()
    return l_dict


def analyze_data(data):
    d = {}
    for key in data:
        for n in data[key]:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1
    return d


if __name__ == "__main__":
    print(get_numbers())
    l = get_multiple_numbers(10000)
    print(l)
    amount = len(l) * 6
    a = analyze_data(l)
    for i in range(1, 45):
        print(a[i], "\t", i, " \t", round(a[i] / amount * 100, 2), "%")
