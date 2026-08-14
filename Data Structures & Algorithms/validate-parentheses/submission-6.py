class Solution:
    def isValid(self, s: str) -> bool:
            opening_parentheses = ['(', '[', '{']
            closing_parentheses = [')', ']', '}']
            queue = []
            is_valid = True
            if len(s) <= 1:
                is_valid = False
                return is_valid
            for ix, i in enumerate(s):
                if i in opening_parentheses:
                    queue.append(i)
                    if ix == len(s) - 1:
                        if len(queue) > 0:
                            is_valid = False

                if i in closing_parentheses:
                    if len(queue) == 0:
                        is_valid = False
                        return is_valid
                    last_queue = queue[-1]
                    if i == ')' and last_queue == '(':
                        queue.pop()
                        continue
                    elif i == ']' and last_queue == '[':
                        queue.pop()
                        continue
                    elif i == '}' and last_queue == '{':
                        queue.pop()
                        continue
                    else:
                        is_valid = False
                        break
            if len(queue) > 0:
                is_valid = False            
            return is_valid