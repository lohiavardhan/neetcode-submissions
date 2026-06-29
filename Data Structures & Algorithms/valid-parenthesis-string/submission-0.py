class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_cnt = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)
            elif char == ')':
                stack.pop()
            else:
                star_cnt += 1
        
        return len(stack) <= star_cnt