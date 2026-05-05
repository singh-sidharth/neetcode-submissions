class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the least possible matrix is 1x1
        # so we can reduce search space of matrix by choosing the target then searching inside it
        # Narrow down the row then narrow down within the search space

        leftR = 0
        rightR = len(matrix)-1
        searchBucket = 0
        midR = 0
        while leftR<=rightR:
            midR = leftR + (rightR-leftR)//2
            # It found the search bucket
            if target >= matrix[midR][0] and target <= matrix[midR][-1]:
                searchBucket = midR
                # Perform binary search in this one
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
            elif target < matrix[midR][0]:
                rightR = midR-1
            else:
                leftR = midR+1
        return False