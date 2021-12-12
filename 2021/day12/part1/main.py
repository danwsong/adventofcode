edges = open('input.txt').read().split('\n')

graph = {}

def is_small_cave(loc):
    return loc.lower() == loc

def count_paths(graph, cur, visited):
    if cur == 'end':
        return 1
    visited.add(cur)
    paths = 0
    for neighbour in graph[cur]:
        if not is_small_cave(neighbour) or neighbour not in visited:
            paths += count_paths(graph, neighbour, visited.copy())
    return paths

for edge in edges:
    l, r = edge.split('-')
    graph[l] = graph.get(l, []) + [r]
    graph[r] = graph.get(r, []) + [l]

print(count_paths(graph, 'start', set()))
