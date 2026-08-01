class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        choco1=float('inf')
        choco2=float('inf')
        for i in range(0,len(prices)):
            if prices[i]<choco1:
                choco1=prices[i]
        prices.remove(choco1)
        for i in range(0,len(prices)):
            if prices[i]<choco2:
                choco2=prices[i]
        result=choco1+choco2
        return money-result if money>=result else money