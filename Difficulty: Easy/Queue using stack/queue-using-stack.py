#User function Template for python3

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, X):
        self.s1.append(X)

    def dequeue(self):
        if not self.s1 and not self.s2:
            return -1
        
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends