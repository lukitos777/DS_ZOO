from .base import DataStructure
from typing import Union, Any


class _Node():
	def __init__(self, val: Any):
		self.val: Any = val
		self.next = None


class LinkedList(DataStructure):
	def __init__(self):
		super().__init__("<class 'LinkedList'>")
		self._head = None

	def add_el(self, val: Any):
		new_node = _Node(val)
		if not self._head:
			self._head = new_node
			self._lehght += 1
			return

		node = self._head
		while node.next is not None:
			node = node.next
		node.next = new_node
		self._lehght -= 1

	def values(self) -> list:
		dp = []
		node = self._head
		while node.next is not None:
			dp.append(node.val)
			node = node.next
		dp.append(node.val)
		return dp

	def insertAtBegin(self, data: Any):
    	new_node = _Node(data)
    	if self.head is None:
        	self.head = new_node
        	return
    	else:
        	new_node.next = self.head
        	self.head = new_node

	def insert(self, index: int, data: Any):
		new_node = _Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None: 
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                raise IndexError

    def inserAtEnd(self, data: Any):
    	new_node = _Node(data)
    	if self.head is None:
        	self.head = new_node
        	return
 
    	current_node = self.head
    	while(current_node.next):
        	current_node = current_node.next
 
    	current_node.next = new_node

    def updateNode(self, index: int, val: Any):
    	if not isinstance(index, int):
    		raise IndexError

    	current_node = self.head
    	position = 0
    	if position == index:
        	current_node.data = val
    	else:
        	while(current_node != None and position != index):
            	position += 1
            	current_node = current_node.next
 
        	if current_node != None:
            	current_node.data = val
        	else:
            	raise IndexError


	def remove_first_node(self):
    	if(self.head == None):
        	return
     
    	self.head = self.head.next

    def pop_node(self):
    	if self.head is None:
        	return
 
    	current_node = self.head
    	while(current_node.next.next):
        	current_node = current_node.next
 
    	current_node.next = None

    def remove(self, index: int):
    	if isinstance(index, int):
    		raise IndexError

        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                raise IndexError

    def remove_node(self, data: Any):
    	current_node = self.head
 
    	while(current_node != None and current_node.next.data != data):
        	current_node = current_node.next
 
    	if current_node == None:
        	return
    	else:
        	current_node.next = current_node.next.next

    def get_length(self):
    	size = 0
    	if(self.head):
        	current_node = self.head
        	while(current_node):
            	size = size+1
            	current_node = current_node.next
        	return size
    	else:
        	return 0

    def search(self, val: Any) -> int:
    	if not self._head:
    		return -1

    	index = 0	
    	node = self._head
    	while node.val != val:
    		if node.next is None and node.val != val:
    			return -1
    		node = node.next
    		index += 1
    	return index

	def get_type(self) -> str:
		return self._type