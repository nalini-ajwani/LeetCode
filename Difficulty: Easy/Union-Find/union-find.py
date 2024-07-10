#User function Template for python3


class Solution:
    def find(self, x, par):
        if par[x] != x:
            par[x] = self.find(par[x], par)
        return par[x]
    
    #Function to merge two nodes a and b.
    def union_(self,a,b,par,rank1):
        # code here
        rootA = self.find(a, par)
        rootB = self.find(b, par)
        if rootA != rootB:
            if rank1[rootA] > rank1[rootB]:
                par[rootB] = rootA
            elif rank1[rootA] < rank1[rootB]:
                par[rootA] = rootB
            else:
                par[rootB] = rootA
                rank1[rootA] += 1
        
    #Function to check whether 2 nodes are connected or not.
    def isConnected(self,x,y,par,rank1):
        # code here
        return self.find(x, par) == self.find(y, par)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        q = int(input())

        par = [i for i in range(n+1)] # parent of ith node is initialized as i.
        rank1 = [1 for i in range(n+1)] # rank is initialized as 1 fo every node
        obj = Solution()
        for i in range(q):
            task,u,v = map(str,input().strip().split())
            u = int(u)
            v = int(v)

            if task == 'U':
                obj.union_(u,v,par,rank1)
            else:
                if obj.isConnected(u,v,par,rank1):
                    print(1)
                else:
                    print(0)


# } Driver Code Ends