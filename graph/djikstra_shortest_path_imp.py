



import sys


class ShortestPath(object):

    def __init__(self, graph):
        if graph is None:
            raise TypeError('graph cannot be None')
        self.graph = graph
        self.previous = {}  # Key: node key, val: prev node key, shortest path
        self.path_weight = {}  # Key: node key, val: weight, shortest path
        self.remaining = PriorityQueue()  # Queue of node key, path weight
        for key in self.graph.nodes.keys():
            # Set each node's previous node key to None
            # Set each node's shortest path weight to infinity
            # Add each node's shortest path weight to the priority queue
            self.previous[key] = None
            self.path_weight[key] = sys.maxsize
            self.remaining.insert(
                PriorityQueueNode(key, self.path_weight[key]))

    def find_shortest_path(self, start_node_key, end_node_key):
        if start_node_key is None or end_node_key is None:
            raise TypeError('Input node keys cannot be None')
        if (start_node_key not in self.graph.nodes or
                end_node_key not in self.graph.nodes):
            raise ValueError('Invalid start or end node key')
        # Set the start node's shortest path weight to 0
        # and update the value in the priority queue
        self.path_weight[start_node_key] = 0
        self.remaining.decrease_key(start_node_key, 0)
        while self.remaining:
            # Extract the min node (node with minimum path weight)
            # from the priority queue
            min_node_key = self.remaining.extract_min().obj
            min_node = self.graph.nodes[min_node_key]
            # Loop through each adjacent node in the min node
            for adj_key in min_node.adj_nodes.keys():
                # Node's path:
                # Adjacent node's edge weight + the min node's
                # shortest path weight
                new_weight = (min_node.adj_weights[adj_key] +
                    self.path_weight[min_node_key])
                # Only update if the newly calculated path is
                # less than the existing node's shortest path
                if self.path_weight[adj_key] > new_weight:
                    # Set the node's previous node key leading to the shortest path
                    # Update the adjacent node's shortest path and
                    # update the value in the priority queue
                    self.previous[adj_key] = min_node_key
                    self.path_weight[adj_key] = new_weight
                    self.remaining.decrease_key(adj_key, new_weight)
        # Walk backwards to determine the shortest path:
        # Start at the end node, walk the previous dict to get to the start node
        result = []
        current_node_key = end_node_key
        while current_node_key is not None:
            result.append(current_node_key)
            current_node_key = self.previous[current_node_key]
        # Reverse the list
        return result[::-1]
      
      
      
      

      
      import unittest


class TestShortestPath(unittest.TestCase):

    def test_shortest_path(self):
        graph = Graph()
        graph.add_edge('a', 'b', weight=5)
        graph.add_edge('a', 'c', weight=3)
        graph.add_edge('a', 'e', weight=2)
        graph.add_edge('b', 'd', weight=2)
        graph.add_edge('c', 'b', weight=1)
        graph.add_edge('c', 'd', weight=1)
        graph.add_edge('d', 'a', weight=1)
        graph.add_edge('d', 'g', weight=2)
        graph.add_edge('d', 'h', weight=1)
        graph.add_edge('e', 'a', weight=1)
        graph.add_edge('e', 'h', weight=4)
        graph.add_edge('e', 'i', weight=7)
        graph.add_edge('f', 'b', weight=3)
        graph.add_edge('f', 'g', weight=1)
        graph.add_edge('g', 'c', weight=3)
        graph.add_edge('g', 'i', weight=2)
        graph.add_edge('h', 'c', weight=2)
        graph.add_edge('h', 'f', weight=2)
        graph.add_edge('h', 'g', weight=2)
        shortest_path = ShortestPath(graph)
        result = shortest_path.find_shortest_path('a', 'i')
        self.assertEqual(result, ['a', 'c', 'd', 'g', 'i'])
        self.assertEqual(shortest_path.path_weight['i'], 8)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()
