
# https://leetcode.com/problems/path-with-minimum-effort/


class Solution:
    def check_neigh(self, heights, i, j, pre_mov):
        if (j+1 < len(heights[0])):
            right_neigh = heights[i][j+1]
        else:
            right_neigh = pow(2, 31)
        if (j-1 > 0):
            left_neigh = heights[i][j-1]
        else:
            left_neigh = pow(2, 31)
        if (i-1 > 0):
            up_neigh = heights[i-1][j]
        else:
            up_neigh = pow(2, 31)
        if (i+1 < len(heights)):
            down_neigh = heights[i+1][j]
        else:
            down_neigh = pow(2, 31)
            
        
            
        if(i==len(heights)-1 and j+1==len(heights[0])-1):
            return [i, j+1, 'complete']
        
        if(i+1==len(heights)-1 and j==len(heights)):
            return [i+1, j, 'complete']
        
        #print(left_neigh, ' ',right_neigh, ' ', up_neigh, ' ', down_neigh)
        if(pre_mov == 'right'):
            left_neigh = pow(2,31)
        if(pre_mov == 'left'):
            right_neigh = pow(2,31)
        if(pre_mov == 'up'):
            down_neigh = pow(2,31)
        if(pre_mov == 'down'):
            up_neigh = pow(2,31)
             
                
        print('previous = ',pre_mov)
        if(left_neigh <= right_neigh and left_neigh <= up_neigh and left_neigh <= down_neigh):
            print('left')
            return [i, j-1, 'left']
        if(right_neigh <= left_neigh and right_neigh <= up_neigh and right_neigh <= down_neigh):
            print('right')
            return [i, j+1, 'right']
        if(up_neigh <= right_neigh and up_neigh <= left_neigh and up_neigh <= down_neigh):
            print('up')
            return [i-1, j, 'up']
        if(down_neigh <= right_neigh and down_neigh <= up_neigh and down_neigh <= left_neigh):
            print('down')
            return [i+1, j, 'down']
        
        
        
        
    def minimumEffortPath(self, heights) -> int:
        effort = []
        i=0
        j=0
        prev_move = 'start'
        
        while(i<len(heights) and j<len(heights[0])):
            res = self.check_neigh(heights, i, j, prev_move)
            prev_move = res[2]
            effort.append(heights[res[0]][res[1]])
            
            if(res[2]=='complete'):
                maxx = max(effort)
                return abs(max(effort)-min(effort))
            
            i = res[0]
            j = res[1]
            

 '''
 class Solution {
    public int minimumEffortPath(int[][] heights) {
        // Index Values
        final int ROW=0, COL=1, EFFORT=2;
        // Size of array
        final int rows = heights.length;
        final int cols = heights[0].length;
        // Movement options
        final int[][] deltas = {{0,1},{0,-1},{1,0},{-1,0}};
        // Keep track of visited vertices
		// Space Complexity O(mn)
        boolean visited[][] = new boolean[rows][cols];
        // Keep best value seen - initialize to MAX_INT
		// Space Complexity O(mn)
		// Time Complexity O(mn)
        int[][] best = new int[rows][cols];
        for (int[] b : best)
            Arrays.fill(b, Integer.MAX_VALUE);
        // Priority Queue for Lowest Path
        Queue<int[]> queue = new PriorityQueue<>((int[] v1, int[] v2)->v1[EFFORT]-v2[EFFORT]);
        // Put starting vertex into queue
        best[0][0] = 0;
        queue.add(new int[]{0,0,0});
        // Iterate over priority queue
		// Time Compelxity up to O(mnlog(mn)) as we potentially iterate over all vertices and each vertex is added to priority queue.
		// Space Complexity of Priority Queue is O(mn) and so add and remove times are O(log(mn))
        while (!queue.isEmpty()) {
            // Get Lowest Cost Node
            int[] vertex = queue.remove();
            // Ignore if already seen
            if (visited[vertex[ROW]][vertex[COL]])
                continue;
            // Get current effort
            int effort = vertex[EFFORT];
            // Check if reached end
            if (vertex[ROW]==rows-1 && vertex[COL]==cols-1)
                return effort;
            // Mark vertex as visited
            visited[vertex[ROW]][vertex[COL]] = true;
            // Check cost of move to adjacent vertex
            for (int[] delta : deltas) {
				// Calculate row and column of adjacent node
                int row = vertex[ROW]+delta[ROW];
                int col = vertex[COL]+delta[COL];
                // Only proceed if valid row/column and not previously visited
                if (row>=0 && row<rows && col>=0 && col<cols && !visited[row][col]) {
					// Effort is related to max height difference
                    int veffort = Math.max(effort, Math.abs(heights[row][col]-heights[vertex[ROW]][vertex[COL]]));
					// If we already have a lower effort for this vertex then no need to add it to priority queue
					// because it is already inthe queue with a lower cost
                    if (veffort < best[row][col]) {
                        best[row][col] = veffort;
                        queue.add(new int[]{row, col, veffort});
                    }
                }
            }
        }
        return 0;
    }
}

 '''           