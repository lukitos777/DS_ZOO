from .base import DataStructure 
from typing import Union, Any


class Stack(DataStructure):
	def __init__(self):
		super().__init__("<class 'Stack'>")
		self._stack: list = []

	def add_el(self, el: Any):
		self._stack.append(el)

	def get_type(self) -> str:
		return self._type

	def pop_el(self) -> Union[Any, None]:
		try:
			return self._stack.pop()
		except IndexError:
			return None

	def get_length(self) -> int:
		return len(self._stack)	

	def clear(self):
		self._stack = []

	def add_els(self, lst: list):
		for el in lst:
			self._stack.append(el)	
	
	def info(self) -> list:
		return self._stack