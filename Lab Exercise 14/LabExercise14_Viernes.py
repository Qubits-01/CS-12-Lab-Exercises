def main():
    budget = 5000
    cost = 500  # Cost per edge (one segment to another).
    n = 10  # No. of road segment/s.

    segments = [
        'Home A',
        'Home B',
        'Home C',
        'B C',
        'C D',
        'E F',
        'D E',
        'E G',
        'A G',
        'G H'
    ]

    graph = {}
    for segment in segments:
        segment = segment.split()

        if segment[0] in graph:
            graph[segment[0]].append(segment[1])
        else:
            graph[segment[0]] = [segment[1]]

        if segment[1] not in graph:
            graph[segment[1]] = []

    print(graph)

    valid_destinations = sorted(list(initiate(graph, budget, cost)))
    print(' '.join(valid_destinations))


def initiate(graph, budget, cost):
    path_len = 0
    valid_destinations = set()

    for neighbor in graph['Home']:
        search(graph, neighbor, path_len, budget // cost, valid_destinations)

    return valid_destinations


def search(graph, curr_node, path_len, max_len, valid_destinations):
    path_len += 1

    if path_len >= max_len:
        return False

    if path_len >= 3:
        valid_destinations.add(curr_node)

    for neighbor in graph[curr_node]:
        search(graph, neighbor, path_len, max_len, valid_destinations)

    return False


if __name__ == '__main__':
    main()
