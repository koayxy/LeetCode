class Solution(object):
    def isValid(self, s):
        # list for open brackets count
        stack = []
        # define mapping for brackets
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # pop top element from stack, if empty stack then assign a placeholder
            if char in mapping:
                top = stack.pop() if stack else '#'
                # check if popped open bracket matches bracket mapping
                if mapping[char] != top:
                    return False
            else:
                # if char is open bracket, push to stack
                stack.append(char)

        # expect empty stack if iteration succeeded
        return not stack
