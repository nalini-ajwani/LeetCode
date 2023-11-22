# User function Template for Python3
from collections import deque

class Solution:
    def minThrow(self, N, arr):
        board = {}
        for i in range(0, 2 * N, 2):
            start, end = arr[i], arr[i + 1]
            board[start] = end

        def get_next_moves(cell):
            moves = []
            for i in range(1, 7):
                next_cell = board.get(cell + i, cell + i)
                moves.append(next_cell)
            return moves

        queue = deque([(1, 0)]) 
        visited = set()

        while queue:
            current_cell, throws = queue.popleft()

            if current_cell == 30:
                return throws

            for next_cell in get_next_moves(current_cell):
                if next_cell not in visited:
                    queue.append((next_cell, throws + 1))
                    visited.add(next_cell)

        return -1  


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends