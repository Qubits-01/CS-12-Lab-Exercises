from collections import deque


def main():
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'D'],
        'C': ['B', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D'],
        'F': [],
        'G': ['H'],
        'H': ['G', 'I'],
        'I': ['H']
    }

    pred, level = bsf(graph, 'A')
    print(pred)
    print(level)

    print('Path A to E:', get_path(pred, 'E'))


def bsf(graph, source_v):
    queue = deque([source_v])
    pred = {source_v: None}
    level = {source_v: 0}

    while len(queue) > 0:
        curr = queue.popleft()  # get first element in queue
        neighbors = graph[curr]

        for neighbor in neighbors:
            if neighbor not in pred:
                pred[neighbor] = curr
                level[neighbor] = level[curr] + 1
                queue.append(neighbor)

    return pred, level


def get_path(pred, v):
    path = ''
    while v is not None:
        path = v + path
        v = pred[v]

    return path


# Traverses even disconnected graphs - that is,
# graphs with more than 1 component.
# pred = {}
# level = {}
#
#
# def bfs_runner(G):
#     components = 0
#     for v in G:
#         if v not in pred:
#             components += 1
#         	bfs(G, v)
#     return components
#
# def bfs(G, S):
#     kyu = deque([S])
#     pred[S] = None
#     level[S] = 0
#     while len(kyu) > 0:
#         curr = kyu.popleft()
#         neighbors = G[curr]
#         for neighbor in neighbors:
#             if neighbor not in pred:
#                 pred[neighbor] = curr
#                 level[neighbor] = level[curr] + 1  # added
#                 kyu.append(neighbor)


if __name__ == '__main__':
    main()
