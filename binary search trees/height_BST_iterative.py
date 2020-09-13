

# Remember: The Height of a binary tree is the Depth of the deepest node in the tree.

from collections import deque


# Data structure to store a Binary Tree node
class Node:
	def __init__(self, data, left=None, right=None):
		self.key = data
		self.left = left
		self.right = right


# Iterative function to calculate height of given binary tree
# by doing level order traversal of the tree
def height(root):

	# empty tree has height 0
	if root is None:
		return 0

	# create an empty queue and enqueue root node
	queue = deque()
	queue.append(root)

	height = 0

	# loop till queue is empty
	while queue:

		# calculate number of nodes in current level
		size = len(queue)

		# process each node of current level and enqueue their
		# non-empty left and right child to queue
		while size > 0:
			front = queue.popleft()

			if front.left:
				queue.append(front.left)

			if front.right:
				queue.append(front.right)

			size = size - 1

		# increment height by 1 for each level
		height = height + 1

	return height


if __name__ == '__main__':

	root = Node(15)
	root.left = Node(10)
	root.right = Node(20)
	root.left.left = Node(8)
	root.left.right = Node(12)
	root.right.left = Node(16)
	root.right.right = Node(25)

	print("The height of the binary tree is", height(root))



