class Solution {
    private Map<Character, Set<Character>> graph;
    public String foreignDictionary(String[] words) {
        StringBuilder ans = new StringBuilder();
        Map<Character, Integer> indegree = new HashMap<>();

        this.graph = new HashMap<>();

        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<Character>());
                indegree.putIfAbsent(c, 0);
            }
        }

        for (int i = 1; i < words.length; i++) {
            // w1 is previous word, w2 is next word
            String w1 = words[i - 1], w2 = words[i];
            int minLen = Math.min(w1.length(), w2.length());

            // string of w1 is larger but it already contains
            // w2 as prefix
            if (w1.length() > w2.length() && w1.startsWith(w2)) {
                return "";
            }

            // core logic to build graph now
            for (int j = 0; j < minLen; j++) {
                if (w1.charAt(j) != w2.charAt(j)) {
                    if (!graph.get(w1.charAt(j)).contains(w2.charAt(j))) {
                        graph.get(w1.charAt(j)).add(w2.charAt(j));
                        indegree.merge(w2.charAt(j), 1, Integer::sum);
                        
                    }
                    break;
                }
            }
        }

        Queue<Character> q = new LinkedList<>();

        for (char c : graph.keySet()) {
            if (indegree.get(c) == 0) {
                q.offer(c);
            }
        }

        // cycle detection
        while (!q.isEmpty()) {
            char char_ = q.poll();
            ans.append(char_);
            for (char neighbor : graph.get(char_)) {
                indegree.merge(neighbor, -1, Integer::sum);
                if (indegree.get(neighbor) == 0) {
                    q.offer(neighbor);
                }
            }
        }

        if (ans.length() != indegree.size()) {
            return "";
        }

        return ans.toString();
    }
}
