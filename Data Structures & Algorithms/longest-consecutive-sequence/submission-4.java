class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length < 2){
            return nums.length;
        }
        // return the length
        // longest consecutive sequence of elements
        // that can be formed
        // next state depends on previous seen
        // Sliding Window + dp 
        int maxLength = 0;

        Set<Integer> set = new HashSet<>();

        for (int num: nums){
            set.add(num);
        }

        for (int num: set){
            //only start if it's the beginning
            if(!set.contains(num-1)){
                int curr = num;
                int length = 1;

                while(set.contains(curr+1)){
                    length++;
                    curr++;
                }

                maxLength = Math.max(maxLength, length);
            }
        }

        return maxLength;
    }
}
