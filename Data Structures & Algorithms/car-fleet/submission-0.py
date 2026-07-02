class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(pos,spe) for pos,spe in zip(position,speed)]
        pair.sort(reverse=True)
        prevTime=(target-pair[0][0])/pair[0][1]
        fleet=1
        for i in range(len(pair)):
            currentcar=pair[i]
            currentTime=(target-currentcar[0])/currentcar[1]
            if currentTime>prevTime:
                fleet+=1
                prevTime=currentTime
        return fleet 
        