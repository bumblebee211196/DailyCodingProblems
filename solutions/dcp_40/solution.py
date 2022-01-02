def solution(arr):
    bin_arr = [0] * 64
    for _, v in enumerate(arr):
        for i in range(64):
            bit = v >> i & 1
            bin_arr[i] = (bin_arr[i] + bit) % 3
    b = "".join(list(map(str, bin_arr[::-1])))
    return int(b, 2)


assert solution([6, 1, 3, 3, 3, 6, 6]) == 1
assert solution([13, 19, 13, 13]) == 19
assert solution([1, 1, 13, 1, 13, 5, 5, 2, 13, 5]) == 2
