#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        from typing import List
from queue import Queue

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # Initialize a visited array to keep track of visited nodes.
        visited = [False] * V

        # Initialize a queue for BFS traversal.
        queue = Queue()

        # Add the starting node (0th vertex) to the queue and mark it as visited.
        queue.put(0)
        visited[0] = True

        # List to store the BFS traversal result.
        bfs_result = []

        # Perform BFS traversal until the queue is empty.
        while not queue.empty():
            # Get the front element from the queue.
            vertex = queue.get()
            bfs_result.append(vertex)

            # Explore all adjacent vertices of the current vertex.
            for adjacent_vertex in adj[vertex]:
                # If the adjacent vertex is not visited, mark it as visited and enqueue it.
                if not visited[adjacent_vertex]:
                    queue.put(adjacent_vertex)
                    visited[adjacent_vertex] = True

        return bfs_result



#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends