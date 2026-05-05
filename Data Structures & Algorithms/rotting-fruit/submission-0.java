class Solution {
    static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int orangesRotting(int[][] grid) {
        int freshCount = 0;
        int timer = 0;


        Deque<int[]> q = new ArrayDeque<>();
        int[][] visited = new int[grid.length][grid[0].length];
        // count fresh and queue up all rotten oranges
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[r].length; c++) {
                if (grid[r][c] == 1) {
                    freshCount++;
                }
                if (grid[r][c] == 2){
                    q.offer(new int[] {r, c});
                    visited[r][c] = 1;
                }
            }
        }
        while (!q.isEmpty() && freshCount > 0) {
            int size = q.size();
            timer++;
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                int r = curr[0];
                int c = curr[1];
                
                for (int[] dir : DIRS) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                    if (nr < 0 || nr >= grid.length || nc < 0 || nc >= grid[0].length
                        || visited[nr][nc] == 1) {
                        continue;
                    }
                    if(grid[nr][nc] == 1){
                        // mark as rotten
                        grid[nr][nc] = 2;
                        freshCount--;
                        visited[nr][nc] = 1;
                        q.offer(new int[]{nr, nc});
                    }
                    
                    
                }
            }
        }


        return freshCount > 0 ? -1 : timer;
    }
}
