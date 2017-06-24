def get_numbers():
    f = open("quicksort.txt", "r").read().splitlines()
    return [int(n) for n in f]


def quick_sort(a, l, r):
    """
    :param a: unsorted array
    :param l: left most index
    :param r: right most index
    :return: inplace sorted array

    Algorithm:

    1. GO: r - l = we have more than one element (more correct because 1 element is sorted), or l < r
    2. get a pivot from the sub array
    3. get left subarray from left most to element before the pivot (remember that python stops 1 before right)
    4. get right subarray from one right of the pivot to the end
    """
    if r - l > 1:
        count[0] += r - l - 1
        p = median_choose_pivot(a, l, r)
        quick_sort(a, l, p)
        quick_sort(a, p+1, r)


def left_choose_pivot(a, l, r):
    """
    :param a: unsorted subarray
    :param l: left most index
    :param r: right most index
    :return: pivot index

    Algorithm:
    1. get the left most element as the pivot
    2. Use i as place marker for swap
    3. go from left most index (not including pivot) to the right
    4. Swap if the element is less/equal to pivot and increment place marker i for swap
    5. Sorting is finished. We have to swap the pivot to it's right place and return the pivot location.
    # NOTE: we use i - 1 because of the looping increments one place forward, and if p is not swapped (
    # the pivot was the smallest element).
    """


    p = a[l]
    i = l + 1
    for j in range(l+1, r):
        if a[j] <= p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1


def right_choose_pivot(a, l, r):
    """
    :param a: unsorted subarray
    :param l: left most index
    :param r: right most index
    :return: pivot index

    Algorithm:
    1. same as left choose pivot, but we swap the right most element to the left
    """

    a[l], a[r-1] = a[r-1], a[l]
    p = a[l]
    i = l + 1
    for j in range(l+1, r):
        if a[j] <= p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1

    return i


def get_median(a, l, r):
    """
    :param a: subarray
    :param l: left most index
    :param r: right most index
    :return: get the median of the left, right, and middle elements, returns an tuple (element,index)
    """
    first = (a[l], l)
    m = l + (r - 1 -l) // 2
    middle = (a[m], m)
    last = (a[r-1], r-1)
    return sorted([first, middle, last])[1]


def median_choose_pivot(a, l, r):
    """
    :param a: subarray
    :param l: left most index of subarray
    :param r: right most index of subarray
    :return: a sorted subarray

    Algorithm:
    1. Same as the left_choose_pivot ,but it finds the median element and then switches that element with the left most element
    """
    med = get_median(a, l, r)

    a[l], a[med[1]] = a[med[1]], a[l]
    p = a[l]

    i = l + 1
    for j in range(l+1, r):
        if a[j] <= p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return i - 1


if __name__ == '__main__':
    """
    The subroutine pivot in the quicksort function can changed with left_choose_pivot, right_choose_pivot, or
    median_choose_pivot
    """
    count = [0]
    a = get_numbers()
    quick_sort(a, 0, len(a))
    print count[0]