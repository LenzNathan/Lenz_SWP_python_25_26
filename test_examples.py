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


if __name__ == "__main__":
    main()
    str
