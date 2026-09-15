class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Thought process documentation:
        ## Restating the question:
        ## This question is asking me that if a given a string build a function that will be able to scan that input and output the length of the longest contiguous sequence of characters within a string. Contiguous I think means in a row so all the characters must be in a row. 
        ## Bute force:
        ## My mind would initially go to utilizing two for-loop which where the first for-loop would loop only once through the entire string. The second for-loop would run every time the first for-loop moves to the next character in the string and keeps going until it either reaches the end of the string or find a repeating character. However, this would not be the most optimal solution because it would have an O(n^2) time complexity since the inner loop runs through for every step the outer loop takes.

        ## More Optimal Solution:
        ## The more optimal solution that I would use is utilizing two pointers. One pointer keeps moving through every iteration of the loop. The one on the left only moves if a duplicate character is found. Every iteration would keep track of the current length by doing r - l. When we have to move the left pointer is when we would check it with the current maximum length.

        maxLen = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen