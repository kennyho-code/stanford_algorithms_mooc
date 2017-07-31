def two_sum(number_file, n1, n2):
    """
    Get number of t between n1 and n2 (inclusive), in which two unique integers x and y equal to t from
    numbers in number_file
    """

    numbers = set()
    with open(number_file) as f:
        for l in f:
            n = int(l.strip())
            numbers.add(n)

    seen = set()
    for x in numbers:
        for n in range(n1, n2+1):
            y = n - x
            if x != y and y in numbers:
                seen.add(n)

    return len(seen)


if __name__ == '__main__':
    print two_sum('numbers.txt', -10000,10000)