class Solution:
    def isHappy(self, n: int) -> bool:
        def in_cycle(n: int, prev: list[int]) -> bool:
            digits = list(map(int, str(n)))
            sum_digits = 0
            for d in digits:
                sum_digits += pow(d, 2)
            if sum_digits == 1:
                return True
            elif sum_digits != 1 and sum_digits in prev:
                return False
            else:
                prev.append(sum_digits)
                return in_cycle(sum_digits, prev)

        return in_cycle(n, [])