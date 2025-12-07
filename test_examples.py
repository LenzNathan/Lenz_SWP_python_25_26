import timeit


def find_pairs(nums, target):
    nums = set(nums)
    pairs = []
    for num in nums:
        for num2 in nums:
            if num + num2 == target and (num2, num) not in pairs:
                pairs.append((num, num2))
    if len(pairs) == 0:
        return None
    return pairs


def print_pairs(pairs):
    if pairs is None:
        print("No pairs found")
    else:
        print(pairs)


def main():
    nums = [1, 2, 6, 3, 4, 6, 7, 8, 9, 10]
    target = 10
    pairs = find_pairs(nums, target)
    print_pairs(pairs)


f = lambda x: x * x


def lambda_test():
    s = 0
    for i in range(10):
        s += f(i)


def standard_test():
    s = 0
    for i in range(10):
        s += i * i


def func(x):
    return x * x

def func_test():
    s = 0
    for i in range(10):
        s += func(i)


if __name__ == "__main__":
    # main()
    timer = timeit.Timer(lambda_test)
    print("lambda execution time:", timer.timeit(number=10_000_000), "seconds for 10_000_000 runs")

    timer = timeit.Timer(standard_test)
    print("standard execution time:", timer.timeit(number=10_000_000), "seconds for 10_000_000 runs")

    timer = timeit.Timer(func_test)
    print("function execution time:", timer.timeit(number=10_000_000), "seconds for 10_000_000 runs")
