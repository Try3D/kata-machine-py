from exercises.djikstras import dijkstra_shortest_path, Graph


def test_dijkstra_single_node():
    graph = Graph()
    graph.add_node("A")
    result = dijkstra_shortest_path(graph, "A")
    assert result == {"A": 0}


def test_dijkstra_simple_graph():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    result = dijkstra_shortest_path(graph, "A")
    assert result == {"A": 0, "B": 1, "C": 3}


def test_dijkstra_disconnected_graph():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_node("C")
    result = dijkstra_shortest_path(graph, "A")
    assert result == {"A": 0, "B": 1, "C": float("inf")}


def test_dijkstra_complex_graph():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("C", "D", 1)
    graph.add_edge("B", "D", 5)
    result = dijkstra_shortest_path(graph, "A")
    assert result == {"A": 0, "B": 1, "C": 3, "D": 4}


def test_dijkstra_no_path():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("C", "D", 1)
    result = dijkstra_shortest_path(graph, "A")
    assert result == {"A": 0, "B": 1, "C": float("inf"), "D": float("inf")}
