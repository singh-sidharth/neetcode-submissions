class Solution {
    public int[] twoSum(int[] nums, int target) {
        // array of integers nums
        // i+j = t
        // i = t-j 
        // store i and check t-j if it exists
        Map<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];
        int n = nums.length;
        for(int i=0; i<n; ++i){
            int difference = target-nums[i];
            if(map.containsKey(difference)){
                ans[0] = map.get(difference);
                ans[1] = i;
                break;
            }
            map.put(nums[i], i);
        }

        return ans;
    }
}
