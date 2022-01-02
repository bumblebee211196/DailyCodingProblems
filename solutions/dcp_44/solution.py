def solution(arr):
    def _solution(arr):
        n = len(arr)
        if n <= 1:
            return 0, arr
        mid = n // 2
        left, left_arr = _solution(arr[:mid])
        right, right_arr = _solution(arr[mid:])
        res_arr = []
        n_left, n_right = len(left_arr), len(right_arr)
        i = j = inversions = 0
        while i < n_left and j < n_right:
            if left_arr[i] < right_arr[j]:
                res_arr.append(left_arr[i])
                i += 1
            else:
                inversions += n_left - i
                res_arr.append(right_arr[j])
                j += 1
        res_arr.extend(left_arr[i:])
        res_arr.extend(right_arr[j:])
        return left + right + inversions, res_arr

    res, _ = _solution(arr)
    return res


assert solution([1, 2, 3, 4, 5]) == 0
assert solution([2, 1, 3, 4, 5]) == 1
assert solution([2, 4, 1, 3, 5]) == 3
assert solution([2, 6, 1, 3, 7]) == 3
assert solution([5, 4, 3, 2, 1]) == 10
