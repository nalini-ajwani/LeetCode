class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        s = []

        for i, temp in enumerate(temperatures):
            while s and temperatures[i] > temperatures[s[-1]]:
                prev_index = s.pop()
                res[prev_index] = i - prev_index
            s.append(i)
        return res