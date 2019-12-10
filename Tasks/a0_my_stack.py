"""
My little Stack
"""
from typing import Any

stack = [1,2,3,4]

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
	global stack
	rmvd = stack.pop()
	print("Popped elem {}".format(rmvd))

	return rmvd


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global stack
	pk = len(stack)
	ind = stack[pk-1]
	print(ind)
	return ind
	#return None


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global stack
	if stack == []:
		return None
	else:
		stack.clear()
	print(stack)
	return None


if __name__ == "__main__":
	#my_list = [1, 2, 4, 5]
	#push(1)
	#pop()
	#peek()
	clear()
	#print(stack)