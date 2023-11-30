from collections import deque
class Solution:
    def is_adj(self, w1, w2):
        diff = sum(c1 != c2 for c1, c2 in zip(w1, w2))
		return diff == 1
	def wordLadderLength(self, startWord, targetWord, wordList):
		#Code here
		if targetWord not in wordList:
		    return 0
		    
		wordSet = set(wordList)
		queue = deque([(startWord, 1)])
		
		while queue:
		    curr, lev = queue.popleft()
		    if curr == targetWord:
		        return lev
		        
		    for word in wordSet.copy():
		        if self.is_adj(curr, word):
		            wordSet.remove(word)
		            queue.append((word, lev + 1))
		            
		return 0
		


#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends