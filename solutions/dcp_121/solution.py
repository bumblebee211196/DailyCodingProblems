from functools import lru_cache


def solution(s: str, k: int) -> bool:
    # @lru_cache(None)
    def dp(l: int, r: int, deleted: int) -> bool:
        # Deleted more than k characters
        if deleted > k:
            return False
        # Reduced to a single character, it is a pallindrome
        if l == r:
            return True
        # Gone out of bounds
        if l > r:
            if l - r == 1:
                return True
            return False
        # Both characters are same
        if s[l] == s[r]:
            res = dp(l + 1, r - 1, deleted)
        # Delete the one at r index or l index
        else:
            res = dp(l + 1, r, deleted + 1) or dp(l, r - 1, deleted + 1)
        return res

    n = len(s)
    return dp(0, n - 1, 0)
