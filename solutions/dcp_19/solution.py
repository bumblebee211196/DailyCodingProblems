import sys


def solution(house_color_prices):
    n, k = len(house_color_prices), len(house_color_prices[0])
    lowest_cost = second_lowest_cost = 0
    lowest_cost_color = -1
    for i in range(n):
        t_lowest_cost = t_second_lowest_cost = sys.maxsize
        t_lowest_cost_color = 0
        for j in range(k):
            if j != lowest_cost_color:
                v = house_color_prices[i][j] + lowest_cost
            else:
                v = house_color_prices[i][j] + second_lowest_cost
            if v < t_lowest_cost:
                t_second_lowest_cost, t_lowest_cost = t_lowest_cost, v
                t_lowest_cost_color = j
            elif v < t_second_lowest_cost:
                t_second_lowest_cost = v
        lowest_cost, second_lowest_cost, lowest_cost_color = t_lowest_cost, t_second_lowest_cost, t_lowest_cost_color
    return lowest_cost


assert solution([
    [10, 8, 11],
    [12, 10, 15],
    [5, 10, 15],
    [25, 15, 18],
    [19, 20, 18]
]) == 58
assert solution([
    [7, 3, 8, 6, 1, 2],
    [5, 6, 7, 2, 4, 3],
    [10, 1, 4, 9, 7, 6]
]) == 4
assert solution([
    [7, 3, 8, 6, 1, 2],
    [5, 6, 7, 2, 4, 3],
    [10, 1, 4, 9, 7, 6],
    [10, 1, 4, 9, 7, 6]
]) == 8
