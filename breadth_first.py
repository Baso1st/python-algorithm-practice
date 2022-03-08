

def get_neighbours(g, node):
    neighbours = []
    for i in range(len(g[node])):
        if g[node][i] == 1:
            neighbours.append(i)
    return neighbours


def bfs(g, at = 0):
    q = []
    visited = [False] * len(g)

    q.append(at)
    visited[at] = True
    print(at)

    while len(q) > 0:
        current = q.pop(0)
        neighbours = get_neighbours(g, current)
        for node in neighbours:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                print(node)


