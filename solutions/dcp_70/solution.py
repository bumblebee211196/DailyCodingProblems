def sum_digits(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num = num // 10
    return digit_sum


def solution(n):
    num = 19
    curr = 1
    while curr < n:
        num += 9
        if (sum_digits(num) == 10):
            curr += 1
    return num
