"""
My little Stack
"""
from typing import Any

stack = []

def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack
	stack.append(elem)  # Add element
	print("Pushed elem {}".format(elem))
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	print(ind)
	return None


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	return None


if __name__ == "__main__":
	#my_list = [1, 2]
	push(1)
	print(stack)