"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])

        result=count=0
        i=j=0
        while i<len(intervals):
            if start[i]<end[j]:
                i+=1
                count+=1
            else:
                j+=1
                count-=1
            result=max(result,count)
        return result