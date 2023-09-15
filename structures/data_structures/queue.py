from .base import DataStructure
from typing import Union, Any


class Queue(DataStructure):
	def __init__(self):
		super().__init__("<class 'Queue'>")
		self._queue: list = []

	def add_el(self, el: Any):
		self._queue.append(el)

	def get_type(self) -> str:
		return self._type

	def get_el(self) -> Union[Any, None]:
		try:
			x: Any = self._queue[0]
			self._queue.remove(x)
			return x
		except IndexError:
			return None

	def add_els(self, lst: list):
		for el in lst:
			self.add_el(el)

	def clear(self):
		self._queue = []

	def info(self) -> list:
		return self._queue

	def get_length(self) -> int:
		return len(self._queue)
