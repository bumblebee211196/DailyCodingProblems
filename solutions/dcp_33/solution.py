import heapq


def solution(arr):
    if not arr:
        return None
    min_heap = []
    max_heap = []
    result = []
    min_heap_count = max_heap_count = 0
    for v in arr:
        heapq.heappush(min_heap, v)
        min_heap_count += 1
        if min_heap_count > max_heap_count + 1:
            popped = heapq.heappop(min_heap)
            min_heap_count -= 1
            heapq.heappush(max_heap, -popped)
            max_heap_count += 1
        if min_heap_count == max_heap_count:
            result.append((min_heap[0] - max_heap[0]) / 2.0)
        else:
            result.append(min_heap[0])
    return result


assert not solution(None)
assert not solution([])
assert solution([2, 5]) == [2, 3.5]
assert solution([3, 3, 3, 3]) == [3, 3, 3, 3]
assert solution([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
