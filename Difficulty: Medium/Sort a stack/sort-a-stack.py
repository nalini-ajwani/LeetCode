class Solution:
    def Sorted(self, s):
        if not s:
            return
        
        top = s.pop()
        
        self.Sorted(s)
        
        self.sortedInsert(s, top)
    
    def sortedInsert(self, s, element):
        if not s or s[-1] <= element:
            s.append(element)
            return
        
        top = s.pop()
        
        self.sortedInsert(s, element)
        
        s.append(top)



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends