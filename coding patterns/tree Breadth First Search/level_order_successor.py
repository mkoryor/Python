

"""

[E] Given a binary tree and a node, find the level order successor of 
the given node in the tree. The level order successor is the node that 
appears right after the given node in the level order traversal.

tree: 
       1
    2   3
  4  5 

given Node: 3
level order successor: 4  
"""




from collections import deque


# TIme: O(N) Space: O(N)
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root is None:
    return None

  queue = deque()
  queue.append(root)
  while queue:
    currentNode = queue.popleft()
    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)

    # break if we have found the key
    if currentNode.val == key:
      break

  return queue[0] if queue else None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
