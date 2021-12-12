edges = open('input.txt').read().split('\n')

graph = {}

def is_small_cave(loc):
    return loc.lower() == loc

def count_paths(graph, cur, visited, visited_twice):
    if cur == 'end':
        return 1
    visited.add(cur)
    paths = 0
    for neighbour in graph[cur]:
        if not is_small_cave(neighbour) or neighbour not in visited:
            paths += count_paths(graph, neighbour, visited.copy(), visited_twice)
        elif not visited_twice:
            paths += count_paths(graph, neighbour, visited.copy(), True)
    return paths

for edge in edges:
    l, r = edge.split('-')
    if r != 'start':
        graph[l] = graph.get(l, []) + [r]
    if l != 'start':
        graph[r] = graph.get(r, []) + [l]

print(count_paths(graph, 'start', set(), False))
