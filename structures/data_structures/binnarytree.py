from .base import DataStructure
from typing import Union, Any


class _Node():
	def __init__(self, val: Any):
		self.val = val
		self.left = left
		self.right = right


class BinnaryTree(DataStructure):
	def __init__(self):
		super().__init__("<class 'BinnaryTree'>")
		self._root = None

	def insert(self, data: Any):
		node = _Node(data)
		if not self._root:
			self._root = node
			return 

		cur_node = self._root
		while True:
			if cur_node.val > data:
				if cur_node.left is not None:
					cur_node = cur_node.left
				else:
					cur_node.left = node
					return
			elif cur_node.val < data:
				if cur_node.right is not None:
					cur_node = cur_node.right
				else:
					cur_node.right = node
					return
			else:
				return

    def search(self, data: Any) -> bool:
    	if not self._root:
    		return False

    	cur_node = self._root

    	while True:
    		if cur_node.val > data:
        		if cur_node.left is None:
        			return False
        		else:
        			cur_node = cur_node.left
        	elif cur_node.val < data:
        		if cur_node.right is None:
        			return False
        		else:
        			cur_node = cur_node.right
        	else:
        		return True

    def get_type(self) -> str:
    	return self._type
