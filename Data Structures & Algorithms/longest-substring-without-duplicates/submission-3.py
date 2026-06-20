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
            count=i-j+1
            max_len=max(count,max_len)
        return max_len