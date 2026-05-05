class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The integers are sorted

        # Brute forece just search linearly : O(n)

        # 6/2 = 3

        l=0
        r=len(nums)-1

        while l<=r:
            mid = (r+l)//2
            print(mid, nums[mid])
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1

        return -1