class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // freq {num: count}
        Map<Integer, Integer> freq = new HashMap<>();

       for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new ArrayList[nums.length + 1];

       for(Map.Entry<Integer, Integer> e: freq.entrySet()){
        int num = e.getKey();
        int count = e.getValue();

        // create buckets if not present
        if (buckets[count] == null) {
                buckets[count] = new ArrayList<>();
            }
        buckets[count].add(num);
       }

       int ans[] = new int[k];
       int idx= 0;

       for(int count=buckets.length-1; count>=0 && idx<k; count--){
        //if count is present
        if(buckets[count] != null){
            for(int num : buckets[count]){
                ans[idx++] = num;
                if(idx == k){
                    return ans;
                }
            }
        }
       }

        return ans;
    }
}
