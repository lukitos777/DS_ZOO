from typing import Any


class _Node():
    def __init__(self, val: Any):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree():  
    def __init__(self):
        self._root = None

    def add(self, val: Any):
        if not self._root:
            self._root = _Node(val)
            return
        else:
            node = self._root
            while True:
                if node.val == val:
                    return
                elif node.val < val:
                    if not node.right:
                        node.right = _Node(val)
                        return
                    else:
                        node = node.right
                else:
                    if not node.left:
                        node.left = _Node(val)
                        return
                    else:
                        node = node.left

    def search(self, val: Any) -> bool:
        if not self._root:
            return False
        else:
            node = self._root
            while True:
                if val == node.val:
                    return True
                elif val > node.val:
                    if node.right is None:
                        return False
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        return False
                    else:
                        node = node.left

    def delite(self, val: Any):
    	...