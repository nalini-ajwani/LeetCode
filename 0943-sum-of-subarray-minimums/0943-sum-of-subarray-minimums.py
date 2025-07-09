class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        ple = [-1] * n
        s = []
        for i in range(n):
            while s and arr[s[-1]] > arr[i]:
                s.pop()
            ple[i] = s[-1] if s else -1
            s.append(i)

        nle = [n] * n
        s = []
        for i in range(n - 1, -1, -1):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            nle[i] = s[-1] if s else n
            s.append(i)

        res = 0
        for i in range(n):
            left = i - ple[i]
            right = nle[i] - i
            res += arr[i] * left * right
            res %= MOD
        return res