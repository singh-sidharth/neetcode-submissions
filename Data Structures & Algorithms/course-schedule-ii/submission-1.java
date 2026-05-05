class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] pre : prerequisites) {
             int course = pre[0];
            int prereq = pre[1];

            adj.get(prereq).add(course);

            indegree[course]++;
        }

        Deque<Integer> q = new ArrayDeque<>();
         for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
            }
        }

        int idx = 0;
        int[] output = new int[numCourses];

        while (!q.isEmpty()) {
            int node = q.poll();
            output[idx++] = node;
            for (int nei : adj.get(node)) {
                indegree[nei]--;
                if (indegree[nei] == 0) {
                    q.add(nei);
                }
            }
        }
        return idx == numCourses ? output : new int[0];
    }
}
