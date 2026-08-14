class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = list('abcdefghijklmnopqrstuvwxyz0123466789')

        clear_output = []
        flag = True
        for letter in s.lower():
            if letter in alphabet:
                clear_output.append(letter)
        
        length = int(len(clear_output)/2)
        for i in range(0, length):
            reversed_index = (i + 1) * -1
            if clear_output[i] != clear_output[reversed_index]:
                flag = False
                break
            else:
                flag = True
        return flag
