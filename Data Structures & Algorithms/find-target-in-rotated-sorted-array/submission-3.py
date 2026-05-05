class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)-1

        if n == 0:
            return (0 if (nums[0]==target) else -1)

        # to find the element in inflection point
        def binary_search(start: int, end: int) -> int:

            left = start
            right = end

            while left<=right:
                m = left + (right-left)//2
                
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            return -1

        # if already sorted and not rotated
        if nums[n] > nums[0]:
            return binary_search(0,n)
        
        if target == nums[0]:
            return 0
        elif target == nums[n]:
            return n

        # Find Inflection Point
        low = 0 
        high = n
        while low<=high:

            mid = low + (high-low)//2

            if nums[mid] == target:
                return mid

            # [4,1] -> mid :4
            if nums[mid] > nums[mid+1]:
                # that's the max in array
                if target > nums[mid]:
                    return -1
                elif target < nums[mid] and target > nums[0]:
                    return binary_search(0, mid-1)
                else:
                    return binary_search(mid+1, n)
            # [4,1] -> mid : 1
            if nums[mid-1] > nums[mid]:
                # that's the min in the array
                if target < nums[mid]:
                    return -1
                elif target > nums[mid] and target < nums[n]:
                    return binary_search(mid+1, n)
                else:
                    return binary_search(0,mid-1)
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        # [3,4,1,2]

        # inflection point is 1
        # target can be in range [3,4], [1,2]
        # use this array to search for the element