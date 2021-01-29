from multiprocessing import Pool

from random import uniform


def get_coordinates():
    return uniform(-1, 1), uniform(-1, 1)


def is_inside_circle(coordinate):
    x, y = coordinate[0], coordinate[1]
    return x * x + y * y < 1


def solution(iterations):
    inside_circle = 0
    for _ in range(iterations):
        if is_inside_circle(get_coordinates()):
            inside_circle += 1
    return 4 * inside_circle / iterations


if __name__ == '__main__':
    args = [100000] * 60
    with Pool(8) as pool:
        result = pool.map(solution, args)
    assert round(sum(result) / len(result), 3) == 3.141
