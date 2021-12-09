import math


def toposort(G):
    ordering = []  # holds processed vertices in order
    visited = set([])

    for v in G:
        if v not in ordering:
            dfs_visit(G, v, ordering, visited)

    return ordering.reverse()


def dfs_visit(G, S, ordering, visited):
    stak = [S]
    visited.add(S)
    while len(stak) > 0:
        curr = stak[-1]
        for v in G[curr]:
            if v not in visited:
                visited.add(v)
                stak.append(v)
                break
        if curr == stak[-1]:
            ordering.append(curr)  # add processed vertex to ordering
            stak.pop()


def shortest_paths_dag(G):
    # ordering = toposort(G)  # assume this is defined
    ordering = ['0', '2', '4', '1', '3', '5']
    d = {}
    pred = {v: None for v in G}
    for u in ordering:
        if u not in d:
            d[u] = 0
        d_u = d[u]
        for e in G[u]:
            v, w = e
            d_v = d.get(v, math.inf)
            if d_v > d_u + w:
                d[v] = d_u + w
                pred[v] = u
    return d, pred


# DAG (Directed Acyclic Graph)
G = {
    '0': [('1', 1), ('2', 7)],
    '1': [('3', 9), ('5', 15)],
    '2': [('4', 4)],
    '3': [('5', 5)],
    '4': [('5', 3)],
    '5': []
}


shortest_path = shortest_paths_dag(G)

print(shortest_path)


