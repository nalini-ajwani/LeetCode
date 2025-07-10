class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []

        for char in s:
            if stk and stk[-1][0] == char:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([char, 1])
        result = ''.join(char * count for char, count in stk)
        return result