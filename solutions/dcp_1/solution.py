def solution(arr, k):
    hash_map = {}
    for number in arr:
        if abs(number - k) in hash_map:
            return True
        hash_map[number] = True
    return False
