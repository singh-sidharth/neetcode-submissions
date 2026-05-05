class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the least possible matrix is 1x1
        # so we can reduce search space of matrix by choosing the target then searching inside it
        # Narrow down the row then narrow down within the search space

        leftR = 0
        rightR = len(matrix)-1
        searchBucket = 0
        mid = 0
        while leftR<=rightR:
            mid = leftR + (rightR-leftR)//2
            if target == matrix[mid][0]:
                return True
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
                searchBucket = mid
                break
            elif target < matrix[mid][0]:
                rightR = mid-1
            else:
                leftR = mid+1
        
        # mid will contain the search space
        searchBukcet = mid

        left = 0
        right = len(matrix[searchBucket])-1

        while left<=right:
            mid = left + (right-left)//2

            if target == matrix[searchBucket][mid]:
                return True
            elif target < matrix[searchBucket][mid]:
                right = mid-1
            else:
                left =  mid+1
        return False