#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return False
        count_a = {}
        count_b = {}
        for char in a:
            if char in count_a:
                count_a[char] += 1
            else:
                count_a[char] = 1
        for char in b:
            if char in count_b:
                count_b[char] += 1
            else:
                count_b[char] = 1
                
        return count_a == count_b

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends