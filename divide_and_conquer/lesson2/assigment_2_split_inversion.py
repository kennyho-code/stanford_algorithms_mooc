def get_numbers():
    f = open("numbers.txt", "r").read().splitlines()

    return [int(n) for n in f]


def merge_sort(a, c):
    """
    :param a: array
    :param c: count of inversion
    :return: sorted array
    Merge Sort with inversion count
    """
    if len(a) <= 1:
        return a
    else:
        m = len(a) // 2
        l = merge_sort(a[:m], c)
        r = merge_sort(a[m:], c)
        return merge(l, r, c)


def merge(l, r, c):
    """
    :param l: left array
    :param r: right array
    :param c: inversion count
    :return: sorted array
    """
    res = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

            c[0] += len(l) - i

    if i < len(l):
        res.extend(l[i:])

    if j < len(r):
        res.extend(r[j:])
    return res


if __name__ == "__main__":
    # get numbers from txt file
    a = get_numbers()
    # save count by pass by reference array
    c = [0]
    # merge sort with inversion count
    merge_sort(a, c)
    print c[0]

