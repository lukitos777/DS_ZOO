from .base import DataStructure 
from typing import Union, Any


class Pqueue(DataStructure):
	def __init__(self):
		super().__init__("<class 'Pqueue'>")
		self._pqueue: list = []

	def add_el(self, val: Any, priority: Union[int, float]):
		if not (isinstance(priority, int) or isinstance(priority, float)):
			raise TypeError
		else:
			self._pqueue.append((priority, val))
			self._pqueue.sort()

	def get_type(self) -> str:
		return self._type

	def get_el(self) -> Union[Any, None]:
		try:
			x: tuple = self._pqueue[0]
			self._pqueue.remove(x)
			return x[1]
		except IndexError:
			return None

	def add_els(self, variables: list, priorities: list):
		if len(variables) != len(priorities):
			raise TypeError
		else:
			for el in zip(variables, priorities):
				self.add_el(el[0], el[1])

	def get_length(self) -> int:
		return len(self._pqueue)

	def info(self) -> list:
		return self._pqueue

	def clear(self):
		self._pqueue = []
