class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stk = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stk))
                return

            if openN < n:
                stk.append('(')
                backtrack(openN+1, closedN)
                stk.pop()

            if closedN < openN:
                stk.append(')')
                backtrack(openN, closedN+1)
                stk.pop()

        backtrack(0, 0)
        return res