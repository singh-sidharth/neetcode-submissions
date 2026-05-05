class Solution {
    public int[] productExceptSelf(int[] nums) {
        /**
        * nums = {1, 2, 3, 4}
        * take a prefix product {1, 2, 6, 24}
        * take a postfix product { 1, 24,12,4}
        * ans = {24, 12, 8, 6}
        */
        int n = nums.length;
        int[] prefix = new int[n+1];
        int[] postfix = new int[n+1];

        // intial arrays
        prefix[0] = 1;
        postfix[n] =1;

        // prefix-postfix
        for(int i=0; i<n; i++){
            prefix[i+1] = prefix[i]*nums[i];
            postfix[n-i-1] = postfix[n-i]*nums[n-i-1];
        }

        int[] ans = new int[n];
        for(int i=0; i<n; i++){
            ans[i] = prefix[i]*postfix[i+1];
        }

        return ans;

    }
}  
