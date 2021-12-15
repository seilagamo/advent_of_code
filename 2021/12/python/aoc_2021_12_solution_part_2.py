from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

visited_list = []
start_node = 'start'
end_node = 'end'
count_paths = 0


def depth_first(graph, current_vertex, visited, small_caves_visited):
    visited.append(current_vertex)

    if current_vertex.isupper():
        pass

    elif current_vertex in (start_node, end_node):
        small_caves_visited.add(current_vertex)

    elif current_vertex not in small_caves_visited:
        small_caves_visited.add(current_vertex)

    is_small_caves_visited_twice = \
        any(k for k, count in Counter(visited).items() if count > 1 and k.islower() and k not in (start_node, end_node))

    if current_vertex != end_node:
        for vertex in graph[current_vertex]:
            if vertex.isupper() or \
                    (vertex.islower() and vertex not in small_caves_visited) or \
                    (vertex.islower() and vertex in small_caves_visited and vertex not in (start_node, end_node) and
                     not is_small_caves_visited_twice):
                depth_first(
                    graph, vertex, visited.copy(), small_caves_visited.copy())

    if visited[-1] == end_node:
        visited_list.append(visited)


def main():
    with open(BASE_DIR / '../input.txt') as f:
        # Load input
        rows = f.read().splitlines()

        nodes = set()
        edges = {}
        for edge in rows:
            _edges = edge.split('-')
            nodes = nodes | set(_edges)

            if _edges[0] not in edges:
                edges[_edges[0]] = set()

            if _edges[1] not in edges:
                edges[_edges[1]] = set()
            edges.get(_edges[0]).add(_edges[1])
            edges.get(_edges[1]).add(_edges[0])

        print()
        for edge in edges:
            print(f'{edge}: {edges.get(edge)}')

        small_caves_visited = set()
        depth_first(edges, start_node, [], small_caves_visited)

        print()
        for v_list in visited_list:
            print(v_list)

        print(f'Result: {len(visited_list)}')


if __name__ == '__main__':
    main()
