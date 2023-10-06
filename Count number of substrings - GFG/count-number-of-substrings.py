#User function Template for python3
import collections
class Solution:
    def substrCount(self, s, k):
        def atMostK(s, k):
            count = 0
            left, right = 0, 0
            char_count = [0] * 26  

            while right < len(s):
                if char_count[ord(s[right]) - ord('a')] == 0:
                    k -= 1
                char_count[ord(s[right]) - ord('a')] += 1

                while k < 0:
                    if char_count[ord(s[left]) - ord('a')] == 1:
                        k += 1
                    char_count[ord(s[left]) - ord('a')] -= 1
                    left += 1

                count += right - left + 1
                right += 1

            return count

        return atMostK(s, k) - atMostK(s, k - 1)




#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends