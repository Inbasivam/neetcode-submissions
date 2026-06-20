class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        j=0
        max_len=0
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[j])
                j+=1 
            char.add(s[i])
            max_len=max(max_len,(i-j+1))
        return max_len