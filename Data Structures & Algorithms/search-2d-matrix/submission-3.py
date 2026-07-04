class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i1=0
        j1=len(matrix)-1
        while i1<=j1:
            mid1=(i1+j1)//2
            i2=0
            j2=len(matrix[mid1])-1
            while i2<=j2:
                mid2=(i2+j2)//2
                if matrix[mid1][mid2]==target:
                    return True
                elif matrix[mid1][mid2]>target:
                    j2=mid2-1
                elif matrix[mid1][mid2]<target:
                    i2=mid2+1
            if matrix[mid1][j2]>target:
                j1=mid1-1
            elif matrix[mid1][j2]<target:
                i1=mid1+1
        return False