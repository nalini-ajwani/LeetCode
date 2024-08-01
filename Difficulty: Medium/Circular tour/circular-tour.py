'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        totPetrol = 0
        totDist = 0
        currPetrol = 0
        res = 0
        
        for i in range(n):
            petrol, dist = lis[i]
            totPetrol += petrol
            totDist += dist
            currPetrol += petrol - dist
            
            if currPetrol < 0:
                res = i + 1
                currPetrol = 0
                
        if totPetrol >= totDist:
            return res
        else:
            return -1
        


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends