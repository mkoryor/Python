


from collections import deque


class Dependency(object):

    def __init__(self, node_key_before, node_key_after):
        self.node_key_before = node_key_before
        self.node_key_after = node_key_after
        
        
        
        
        
class BuildOrder(object):

    def __init__(self, dependencies):
        self.dependencies = dependencies
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        for dependency in self.dependencies:
            self.graph.add_edge(dependency.node_key_before,
                                dependency.node_key_after)

    def _find_start_nodes(self, processed_nodes):
        nodes_to_process = {}
        for key, node in self.graph.nodes.items():
            if node.incoming_edges == 0 and key not in processed_nodes:
                nodes_to_process[key] = node
        return nodes_to_process

    def _process_nodes(self, nodes_to_process, processed_nodes):
        for node in nodes_to_process.values():
            # We'll need to iterate on copies since we'll need
            # to change the dictionaries during iteration with
            # the remove_neighbor call
            for adj_node in list(node.adj_nodes.values()):
                node.remove_neighbor(adj_node)
            processed_nodes[node.key] = node
        nodes_to_process = {}

    def find_build_order(self):
        result = []
        nodes_to_process = {}
        processed_nodes = {}
        while len(result) != len(self.graph.nodes):
            nodes_to_process = self._find_start_nodes(processed_nodes)
            if not nodes_to_process:
                return None
            result.extend(nodes_to_process.values())
            self._process_nodes(nodes_to_process, processed_nodes)
        return result
      
      
      
      

      
      
      
import unittest


class TestBuildOrder(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBuildOrder, self).__init__()
        self.dependencies = [
            Dependency('d', 'g'),
            Dependency('f', 'c'),
            Dependency('f', 'b'),
            Dependency('f', 'a'),
            Dependency('c', 'a'),
            Dependency('b', 'a'),
            Dependency('a', 'e'),
            Dependency('b', 'e'),
        ]

    def test_build_order(self):
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()

        expected_result0 = ('d', 'f')
        expected_result1 = ('c', 'b', 'g')
        self.assertTrue(processed_nodes[0].key in expected_result0)
        self.assertTrue(processed_nodes[1].key in expected_result0)
        self.assertTrue(processed_nodes[2].key in expected_result1)
        self.assertTrue(processed_nodes[3].key in expected_result1)
        self.assertTrue(processed_nodes[4].key in expected_result1)
        self.assertTrue(processed_nodes[5].key is 'a')
        self.assertTrue(processed_nodes[6].key is 'e')

        print('Success: test_build_order')

    def test_build_order_circular(self):
        self.dependencies.append(Dependency('e', 'f'))
        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        self.assertTrue(processed_nodes is None)

        print('Success: test_build_order_circular')


def main():
    test = TestBuildOrder()
    test.test_build_order()
    test.test_build_order_circular()


if __name__ == '__main__':
    main()
    
    
    
    
