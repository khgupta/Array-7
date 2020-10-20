#Time complexity : O(n)
#Space complexity: O(1)
#Works on leetcode : yes
#Approach : Here we iterate through the words and whenever the current word matches word1, we update index1 and get the 
#minimum. Next when we find the word2, we do the same as before. 
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        size = len(words)
        i1, i2 = size, size
        ans = size
    
        for i in range(size):
            if words[i] == word1:
                i1 = i
                ans = min(ans, abs(i1-i2))
            elif words[i] == word2:
                i2 = i
                ans = min(ans, abs(i1-i2))
        return ans