class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1>n2:
            self.findMedianSortedArrays(nums2,nums1)
        
        low = 0
        high = n1
        left = (n1+n2+1)//2
        # Handle empty list 2 case, then it is just a simple median problem
        if n2 == 0:
            if n1%2 == 1:
                return nums1[left-1]
            # even
            return (nums1[left] + nums1[left-1])/2
        # Not empty
        while low<=high:
            mid1 = (low+high)>>1
            mid2 = left-mid1
            
            # calculate l1, l2, r1, r2
            r1 = nums1[mid1] if mid1<n1 else float('inf')               
            r2 = nums2[mid2] if mid2<n2 else float('inf')
            l1 = nums1[mid1-1] if mid1-1>=0 else float('-inf')              
            l2 = nums2[mid2-1] if mid2-1>=0 else float('-inf')
                

            # binary search for selecting no. of
            # elements in left sub-array
            if l1<=r2 and l2<=r1:
                # odd
                if (n1+n2)%2 == 1:
                    return max(l1,l2)
                    # even
                return (max(l1,l2)+min(r1,r2))/2
                
            elif l1>r2:
                high = mid1 - 1
                
            else:
                low = mid1 + 1
                