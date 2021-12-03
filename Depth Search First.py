def main():
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['B', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D'],
        'F': [],
        'G': ['H'],
        'H': ['G'],
        'I': ['H']
    }

    dfs(graph)
    print(pred)


pred = {}


def dfs(G):
    for v in G:
        if v not in pred:
            pred[v] = None
            dfs_visit(G, v)


def dfs_visit(G, S):
    stak = [S]
    while len(stak) > 0:
        curr = stak[-1]
        for v in G[curr]:
            if v not in pred:
                pred[v] = curr
                stak.append(v)
                break
        if curr == stak[-1]:  # no newly visited vertices
            stak.pop()


if __name__ == '__main__':
    main()
