def solution(arr):
    if not arr:
        return []
    n = len(arr)
    prefix_product = [0] * n
    prefix_product[0] = arr[0]
    for i in range(1, n):
        prefix_product[i] = arr[i] * prefix_product[i-1]
    suffix_product = [0] * n
    suffix_product[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suffix_product[i] = arr[i] * suffix_product[i+1]
    result = [0] * n
    for i in range(n):
        if i == 0:
            result[i] = suffix_product[i+1]
        elif i == n-1:
            result[i] = prefix_product[i-1]
        else:
            result[i] = prefix_product[i-1] * suffix_product[i+1]
    return result
