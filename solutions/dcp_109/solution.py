def solution(x: int) -> int:
    return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1
