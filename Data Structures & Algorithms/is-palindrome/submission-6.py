import string
class Solution:
    def isPalindrome(self, w: str) -> bool:
        is_palindrome = True
        l_small = string.ascii_lowercase
        l_big = string.ascii_uppercase
        numbers = list(map(lambda x: str(x), list(range(0, 10))))
        is_allowed = lambda x: x in l_big or x in l_small or x in numbers
        filtered_data = filter(is_allowed, w)
        words = ("".join(filtered_data)).lower()
        w = words
        for i in range(0, len(w) // 2):
            start = w[i]
            end = w[-(i + 1)]
            if start != end:
                is_palindrome = False
        return is_palindrome

