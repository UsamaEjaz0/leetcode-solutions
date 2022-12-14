class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for _, arr in enumerate(matrix):
            if target > arr[-1]:
                continue
            else:
                i = 0
                j = len(arr) - 1

                while i <= j:
                    mid = (i + j)//2

                    if target > arr[mid]:
                        i = mid + 1
                    elif target < arr[mid]:
                        j = mid - 1
                    else:
                        return True

                return False
    
        
    
        