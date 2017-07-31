import heapq


# *** Implementation for Max Heap (Python only has min heap)***
def heap_pop_max(heap):
    """
    1. Pop last element in the heap
    2. If it isn't the only element, then the root is the max. Insert the last element to the root and sift up the max element
    3. If it is the last element so just return it
    """
    last = heap.pop()
    if heap:
        return_item = heap[0]
        heap[0] = last
        heapq._siftup_max(heap, 0)
    else:
        return_item = last
    return return_item


def heap_push_max(heap, item):
    """
    1. append to the list
    2. then sift down bigger elements to maintain the invariant

    """
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def median_insert(max_heap, min_heap, e):

    """
    Insert median and rebalance
    """
    if not max_heap and not min_heap:
        heap_push_max(max_heap, e)

    elif max_heap and not min_heap:
        heapq.heappush(min_heap, e)
    else:

        max_e = max_heap[0]
        min_e = min_heap[0]

        if e <= max_e:
            heap_push_max(max_heap, e)

        elif e >= min_e:
            heapq.heappush(min_heap, e)
        else:
            heap_push_max(max_heap, e)

        # re-balance
        if (len(max_heap) - len(min_heap)) > 1:
            e = heap_pop_max(max_heap)
            heapq.heappush(min_heap, e)

        if (len(min_heap) - len(max_heap)) > 1:
            e = heapq.heappop(min_heap)
            heap_push_max(max_heap, e)

    # edge case if boundaries get mixed
    if len(max_heap) == 1 and len(min_heap) == 1 and max_heap[0] > min_heap[0]:
        max_heap[0], min_heap[0] = min_heap[0], max_heap[0]


def get_median(max_heap, min_heap):
    """
    Get median between the two heaps
    """
    e = None
    if len(max_heap) or len(min_heap):
        if len(max_heap) >= len(min_heap):
            e = heap_pop_max(max_heap)
            heap_push_max(max_heap, e)

        else:
            e = heapq.heappop(min_heap)
            heapq.heappush(min_heap, e)
    return e


def running_median(file):

    max_heap = []
    min_heap = []
    res = 0
    with open(file)as f:
        for l in f:
            n = int(l.strip())
            median_insert(max_heap, min_heap, n)
            res += get_median(max_heap, min_heap)

    return res % 10000

if __name__ == '__main__':
    print running_median("numbers.txt")

