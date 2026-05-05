class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # Basically nums[i] + nums[j] = -nums[k]
    # Cut slices of array then use the last index as 0
    # Least case array is size 3

        res: List[List[int]] = []

        nums.sort() # O(nlogn)
        length = len(nums)

        # O(n**2)    
        for i in range(0,length):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = length-1

            while left < right:
                currSum = nums[i]+nums[left] + nums[right]
                if currSum == 0:
                    res.append([nums[i],nums[left], nums[right]])
                    # Continue finding more solutions
                    left+=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                elif currSum < 0:
                    left+=1
                else:
                    right-=1

        return res