

"""
[E] Given a binary tree, return an array containing nodes in its right view. The right view of a 
binary tree is the set of nodes visible when the tree is seen from the right side.

tree:
        1
      2   3
    4  5 6  7 

right view: [1,3,7]
"""


from __future__ import print_function
from collections import deque


# TIme: O(N) Space: O(N)
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
  if root is None:
    return

  queue = deque()
  queue.append(root)
  currentNode, previousNode = None, None
  while queue:
    currentNode = queue.popleft()
    if previousNode:
      previousNode.next = currentNode
    previousNode = currentNode

    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
