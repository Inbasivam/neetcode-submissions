class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)<len(text2):
            text1,text2=text2,text1
        frequency=[0]*(len(text2)+1)
        for i in range(len(text1)-1,-1,-1):
            previous=0
            for j in range(len(text2)-1,-1,-1):
                temporary=frequency[j]
                if text1[i]==text2[j]:
                    frequency[j]=1+previous
                else:
                    frequency[j]=max(frequency[j],frequency[j+1])
                previous=temporary
        return frequency[0]