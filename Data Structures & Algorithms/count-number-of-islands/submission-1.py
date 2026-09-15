from typing import List


class Solution:
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def dfs(self, dir_x: int, dir_y: int, grid: List[List[str]]):
        val = grid[dir_x][dir_y]
        node = str(val) + "_" + str(dir_x) + "_" + str(dir_y)
        if node == "1_0_2":
            print("here")
        if node in self.visited or val == "0":
            return
        if node not in self.visited and val == "1":
            self.visited.add(node)
            print(f"visited {node}")
        for x, y in self.directions:
            next_x = dir_x + x
            next_y = dir_y + y
            if next_x == 0 and next_y == 2:
                print("here I am")
            if (
                next_x >= 0
                and next_x < len(grid)
                and next_y >= 0
                and next_y < len(grid[next_x])
            ):
                self.dfs(next_x, next_y, grid)

    def numIslands(self, grid: List[List[str]]):
        # directions = [(1, -1), (1, 0), (0, 1), (-1, 0)]
        self.visited = set()
        self.visited_islands = 0
        for i in range(0, len(grid)):
            j = grid[i]
            for j in range(0, len(j)):
                if (
                    grid[i][j] == "1"
                    and (grid[i][j] + "_" + str(i) + "_" + str(j)) not in self.visited
                ):
                    self.visited_islands += 1
                    print(
                        f"visited island:  {grid[i][j] + "_" + str(i) + "_" + str(j)}"
                    )
                    self.dfs(i, j, grid)
                else:
                    continue

        return self.visited_islands




                # when we find one it is start of the island.
                # from there we find connections of the island in 4 possible direction
                # at the end we count island 
                 
# The graph represented as an Adjacency List
# graph = { 'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': [] }

# visited = set() # Set to track visited nodes

# # def dfs(node, graph, visited):
# #     if node not in visited:
# #         print(node, end=" ")  # Process the node
# #         visited.add(node)     # Mark as visited
        
# #         # Recursively visit all unvisited neighbors
# #         for neighbor in graph[node]:
# #             dfs(neighbor, graph, visited)

# # Execute the traversal starting at node 'A'
# print("DFS Traversal Order:")
# dfs('A', graph, visited)
# # Output: A B D E C F

