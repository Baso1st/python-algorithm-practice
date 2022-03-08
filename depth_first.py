
from breadth_first import get_neighbours


def dfs(g, at = 0):
    visited = [False] * len(g)
    _dfs(g, visited, at)


def _dfs(g: list, visited: list, at = 0):
    if visited[at]:
        return

    visited[at] = True
    print(at)
    neighbours = get_neighbours(g, at)
    for node in neighbours:
        _dfs(g, visited, node)