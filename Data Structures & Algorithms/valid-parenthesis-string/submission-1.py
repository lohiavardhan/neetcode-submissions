class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_cnt = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                star_cnt += 1
        
        return len(stack) <= star_cnt