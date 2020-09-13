


# Iterative function to perform in-order traversal of the tree
def inorderIterative(root):

	# create an empty stack
	stack = deque()

	# start from root node (set current node to root node)
	curr = root

	# if current node is None and stack is also empty, we're done
	while stack or curr:

		# if current node is not None, push it to the stack (defer it)
		# and move to its left child
		if curr:
			stack.append(curr)
			curr = curr.left
		else:
			# else if current node is None, we pop an element from the stack,
			# print it and finally set current node to its right child
			curr = stack.pop()
			print(curr.data, end=' ')

			curr = curr.right


