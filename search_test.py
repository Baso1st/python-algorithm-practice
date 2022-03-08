
from breadth_first import bfs
from depth_first import dfs


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


g = get_adjacency_matrix()
bfs(g, 0)
print('-'*50)
dfs(g, 0)