"""
route between nodes: an iterative implementation of BFS
graph is represented as a dictionary with keys as nodes and values as the nodes connected to that node
"""


def search(G, start, end):  # G is the graph (dict), start is the starting node(int), end is the end node (int)
	if (start == end): return True

	visited = []

	queue = []  # use a list to implement queue
	queue.append(start)
	while (queue != []):
		u = queue.pop(0)  # this is the node we are looking at now
		if (G[u] != []): 
			for v in G[u]:
				if v is not in visited:
					if v == end:
						return True
					else:
						queue.append(v)
			visitied.append(u)
	return False




	

