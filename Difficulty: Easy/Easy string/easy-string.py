#User function Template for python3

class Solution:
    def transform(self, S: str) -> str:
        S = S.lower()
        compressed = ""
        count = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                count += 1
            else:
                compressed += str(count) + S[i - 1] 
                count = 1
        compressed += str(count) + S[-1] 
        return compressed


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.transform(S))
# } Driver Code Ends