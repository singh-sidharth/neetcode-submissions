class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String,List<String>>();

        for (String str: strs){
            int[] arr = new int[26];
            for(int i=0; i<str.length(); i++){
                arr[str.charAt(i)-'a']++;
            }

            String key = Arrays.toString(arr);
            map.computeIfAbsent(key, k -> new ArrayList<String>());
            map.get(key).add(str);
        }

        return new ArrayList<>(map.values());
    }
}
