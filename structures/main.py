#  from data_structures.stack import *
#  from data_structures.queue import *
#  from data_structures.pqueue import *
#  from data_structures.linkedlist import LinkedList
from data_structures.binnarytree import BinnaryTree 


if __name__ == '__main__':
	tree = BinnaryTree()
	tree.insert(34)
	tree.insert(37)
	tree.insert(32)
	tree.insert(36)
	tree.insert(38)
	tree.insert(33)
	tree.insert(31)
	print(tree.search(36))
	print(tree.search(12))