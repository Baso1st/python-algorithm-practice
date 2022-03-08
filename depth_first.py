
def get_adjacency_matrix():
    adj = []
    # adj.append([0, 1, 1, 0, 0])
    # adj.append([1, 0, 0, 1, 1])
    # adj.append([1, 0, 0, 1, 0])
    # adj.append([0, 1, 1, 0, 0])
    # adj.append([0, 1, 0, 0, 0])

    adj.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    adj.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    adj.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    adj.append([0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0])
    adj.append([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    adj.append([0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0])
    adj.append([0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0])
    adj.append([0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0])
    adj.append([0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0])
    adj.append([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
    adj.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0])
    adj.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0])
    adj.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    return adj



def get_neighbours(g, node):
    neighbours = []
    for i in range(len(g[node])):
        if g[node][i] == 1:
            neighbours.append(i)
    return neighbours


n = 13
visited = [False] * n


g = get_adjacency_matrix()


# print(g)

def dfs(at = 0):
    if visited[at]:
        return

    visited[at] = True
    print(at)
    neighbours = get_neighbours(g, at)
    for node in neighbours:
        dfs(node)


dfs(11)
