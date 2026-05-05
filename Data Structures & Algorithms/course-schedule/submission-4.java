class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        List<List<Integer>> graph = new ArrayList<>();

        int[] indegree = new int[numCourses];

        for(int i = 0; i<numCourses; i++){
            graph.add(new ArrayList<>());
        }

        for(int[] req: prerequisites){
            graph.get(req[1]).add(req[0]);
            indegree[req[0]] +=1;
        }

        Deque<Integer> q = new ArrayDeque<>();

        for(int i=0; i<numCourses; i++){
            if(indegree[i] == 0) q.offer(i);
        }

        int completed = 0;

        while(!q.isEmpty()){
            int curr = q.poll();
            completed++;
            for(int nei : graph.get(curr)){
                indegree[nei]--;
                
                if(indegree[nei] == 0){
                    q.offer(nei);
                }
            }
        }

       return completed == numCourses;
    }
}
