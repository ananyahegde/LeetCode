class Solution:
    def hash(self, open, close):
        map = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        return close == map[open]

    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                print(c)
                stk.append(c)

            if c == ')' or c == '}' or c == ']':
                print(c)
                if stk:
                    print(stk)
                    top = stk.pop()
                    if not self.hash(top, c):
                        return False
                else:
                    return False

        if stk:
            return False
        return True

x = Solution()
print(x.isValid("(){}}{"))