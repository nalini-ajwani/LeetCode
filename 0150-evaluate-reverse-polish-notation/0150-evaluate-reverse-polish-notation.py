class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for char in tokens:
            if char in {"+", "-", "*", "/"}:
                b = s.pop()
                a = s.pop()

                if char == '+':
                    s.append(a+b)
                elif char == '-':
                    s.append(a-b)
                elif char == '*':
                    s.append(a*b)
                elif char == '/':
                    s.append(int(a/b))
            else:
                s.append(int(char))

        return s[0]