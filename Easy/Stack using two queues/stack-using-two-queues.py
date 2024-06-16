#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue

queue_1 = Queue()
queue_2 = Queue()

def push(x):
    if not queue_1.empty() or (queue_1.empty() and queue_2.empty()):
        queue_1.put(x)
    else:
        queue_2.put(x)
 
def pop():
    if not queue_1.empty():
        while queue_1.qsize() > 1:
            queue_2.put(queue_1.get())
        return queue_1.get()
    elif not queue_2.empty():
        while queue_2.qsize() > 1:
            queue_1.put(queue_2.get())
        return queue_2.get()
    else:
        return -1 



#{ 
 # Driver Code Starts

from queue import Queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        queue_1 = Queue() # first queue
        queue_2 = Queue() # second queue
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                push(a[i+1])
                i+=1
            else:
                print(pop(),end=" ")
            i+=1
            
        print()
# } Driver Code Ends