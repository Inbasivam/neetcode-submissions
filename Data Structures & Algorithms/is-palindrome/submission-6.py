class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            while i < j and not self.AlphaNum(s[i]):
                i += 1
            while i < j and not self.AlphaNum(s[j]):
                j -= 1
                
            if s[i].lower() != s[j].lower():
                return False
            
            i, j = i + 1, j - 1  
            
        return True

   
    def AlphaNum(self, x: str) -> bool:
        return (
            (ord('A') <= ord(x) <= ord('Z')) or 
            (ord('a') <= ord(x) <= ord('z')) or 
            (ord('0') <= ord(x) <= ord('9'))
        )