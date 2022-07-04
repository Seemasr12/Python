from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):
		visited.add(v)
		print(v, end=' ')
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)
	def DFS(self, v):
		visited = set()
		self.DFSUtil(v, visited)
m = Graph()
m.addEdge(0, 1)
m.addEdge(0, 2)
m.addEdge(1, 2)
m.addEdge(2, 0)
m.addEdge(2, 3)
m.addEdge(3, 3)
print("DFS(starting from vertex 2)")
m.DFS(2)
