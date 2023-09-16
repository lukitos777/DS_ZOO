from bintree import BinaryTree


if __name__ == '__main__':
	tree = BinaryTree()
	tree.add(15)
	tree.add(12)
	tree.add(13)
	tree.add(11)
	tree.add(19)
	tree.add(20)
	tree.add(17)
	print(tree.search(19))
	# tree.delite(19)
	print(tree.search(19))