import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        result=i
        while i<=j:
            mid=(i+j)//2
            tT=0
            for p in piles:
                tT+=math.ceil(p/mid)
            if tT<=h:
                result=mid
                j=mid-1
            else:
                i=mid+1
        return result