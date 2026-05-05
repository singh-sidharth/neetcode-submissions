class Solution {
    public int trap(int[] heights) {
        int n = heights.length;
        int l = 0;
        int r = n-1;
        int left = heights[l];
        int right = heights[r];
        int ans = 0;
        
        while(l<r){

            if(heights[l] <= heights[r]){
                left = Math.max(heights[l], left);
                int water = left-heights[l];
                ans+=water;
                l++;
            }
            else{
                right = Math.max(heights[r], right);
                int water = right-heights[r];
                ans+=water;
                r--;
            }
        }

        return ans;
    }
}
