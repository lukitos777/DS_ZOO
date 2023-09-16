from graph import Graph 


if __name__ == '__main__':
	g = Graph()
	g.add_way('a', 'b')
	g.add_way('b', 'c')
	g.add_way('b', 'd')
	
	g.add_way('a', 'f')
	g.get_graph()
	print(g.DFS('d', 'b'))
	print(g.DFS('f', 'b'))