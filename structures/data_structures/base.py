from abc import ABC, abstractmethod


class DataStructure(ABC):
	def __init__(self, structure_type: str):
		self._type = structure_type

	@abstractmethod
	def get_type(self):
		pass