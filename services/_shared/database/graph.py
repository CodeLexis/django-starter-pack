from typing import Any, Dict, List

from gremlin_python.structure.graph import Graph, Edge, Vertex
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import Cardinality, within


class GremlinClient(object):
    def __init__(self, url: str, *args, **kwargs):
        self.connection = DriverRemoteConnection(url, 'g')
        self.graph = Graph().traversal().withRemote(self.connection)

    def add_edge(self, edge_name: str, vertex_1, vertex_2, properties: Dict[str, Any] = None) -> Edge:
        edge = self.graph.V(vertex_1).add_e(edge_name)
        
        if properties:
            for k, v in properties.items():
                edge.property(k, v)

        return edge.to(vertex_2).next()

    def add_node(self, class_name: str, properties: Dict[str, Any] = None) -> Vertex:
        vertex = self.graph.add_v(class_name)

        if properties:
            for k, v in properties.items():
                if type(v) is list:
                    for val in v:
                        vertex = vertex.property(Cardinality.list_, k, val)

                else:
                    vertex.property(k, v)

        return vertex.next()

    def clean(self):
        self.graph.E().drop().iterate()
        self.graph.V().drop().iterate()
    
    def close(self):
        self.connection.close()

    def get_nodes(self, class_name: str, properties: Dict[str, Any] = None) -> List[Vertex]:
        traversal = self.graph.V().has_label(class_name)

        _props = []
        if properties is not None:
            for k, v in properties.items():
                if type(v) is list:
                    v = within(v)

                _props.extend([k, v])

        if _props:
            traversal = traversal.has(*_props)

        return traversal.to_list()

    def get_neighbour_nodes(self, node) -> List[Vertex]:
        return self.graph.V(node).bothE().as_('e').otherV().as_('v').select('e', 'v').toList()

    def get_nodes_with_edge(self, edge_name: str) -> List[Vertex]:
        return self.graph.V().both_e().has_label(edge_name).other_v().toList()
