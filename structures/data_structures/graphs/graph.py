from typing import Union
from pprint import pprint


class Graph():
	def __init__(self):
		self._graph = dict()

	def add_way(self, A: Union[int, str], B: Union[int, str]):
		if not ((isinstance(A, str) or isinstance(A, int)) and\
			(isinstance(B, str) or isinstance(B, int))):
			raise TypeError

		if A not in self._graph.keys():
			self._graph[A] = [B]
		else:
			self._graph[A].append(B)

		if B not in self._graph.keys():
			self._graph[B] = []

	def BFS(self, target: Union[int, str], start: Union[int, str]) -> bool:
		if start not in self._graph.keys():
			raise ValueError
		else:
			visited, queue = [], []
			visited.append(start)
			queue.append(start)

			while queue:
				vertix = queue.pop(0)
				if vertix not in self._graph.keys():
					continue
				for neighbour in self._graph[vertix]:
					if neighbour == target:
						return True
					else:
						visited.append(neighbour)
						queue.append(neighbour)
			return False

	def _helper(self, target, start, visited=set()) -> set:
		visited.add(start)
		for node in self._graph[start]:
			if node not in visited:
				self._helper(target, node, visited)
		return visited

	def DFS(self, target: Union[int, str], start: Union[int, str], visited=set()) -> bool:
		if start not in self._graph.keys():
			raise ValueError
		else:
			return target in self._helper(target, start)
		
	def get_graph(self):
		pprint(self._graph)