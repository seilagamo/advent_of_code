from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

visited_list = []
start_node = 'start'
end_node = 'end'


def depth_first(graph, current_vertex, visited, small_caves_visited):
    visited.append(current_vertex)
    if current_vertex.islower():
        small_caves_visited.add(current_vertex)

    for vertex in graph[current_vertex]:
        if vertex not in small_caves_visited:
            depth_first(graph, vertex, visited.copy(), small_caves_visited.copy())

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

        small_caves_visited = set()
        depth_first(edges, start_node, [], small_caves_visited)

        print()
        for v_list in visited_list:
            print(v_list)

        print(f'Result: {len(visited_list)}')


if __name__ == '__main__':
    main()
