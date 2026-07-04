class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        count_t={}
        for i in t:
            count_t[i]=1+count_t.get(i,0)
        res=[-1,-1]
        res_length=float('infinity')
        have=0
        need=len(count_t)
        l=0
        for r in range(len(s)):
            x=s[r]
            window[x]=1+window.get(x,0)
            if x in count_t and window[x]==count_t[x]:
                have+=1
            while have==need:
                if r-l+1<res_length:
                    res=[l,r]
                    res_length=r-l+1
                window[s[l]]-=1
                if s[l] in count_t and window[s[l]]<count_t[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res_length!=float('infinity') else ""    