import heapq
import math


def main():
    graph_1 = {
        'A': [('B', 153), ('C', 232), ('D', 123)],
        'B': [('A', 153), ('D', 12), ('J', 14)],
        'C': [('A', 232), ('L', 932)],
        'D': [('A', 123), ('B', 12), ('G', 123), ('J', 132)],
        'E': [('F', 122), ('H', 213), ('I', 232), ('L', 23)],
        'F': [('E', 122), ('G', 1134), ('I', 153), ('K', 23), ('L', 98)],
        'G': [('D', 123), ('F', 1134), ('J', 13), ('L', 23)],
        'H': [('E', 213), ('I', 985)],
        'I': [('E', 232), ('F', 153), ('H', 985), ('K', 172)],
        'J': [('B', 14), ('D', 132), ('G', 13)],
        'K': [('F', 23), ('I', 172)],
        'L': [('C', 932), ('E', 23), ('F', 98), ('G', 23)]
    }

    edges = {
        ('A', 'B'): 153,
        ('A', 'C'): 232,
        ('A', 'D'): 123,
        ('B', 'D'): 12,
        ('B', 'J'): 14,
        ('C', 'L'): 932,
        ('D', 'G'): 123,
        ('D', 'J'): 132,
        ('E', 'F'): 122,
        ('E', 'H'): 213,
        ('E', 'I'): 232,
        ('E', 'L'): 23,
        ('F', 'G'): 1134,
        ('F', 'I'): 153,
        ('F', 'K'): 23,
        ('F', 'L'): 98,
        ('G', 'J'): 13,
        ('G', 'L'): 23,
        ('H', 'I'): 985,
        ('I', 'K'): 172,
    }

    graph_2 = {}
    for edge in edges:
        graph_2.setdefault(edge[0], []).append((edge[1], edges[edge]))
        graph_2.setdefault(edge[1], []).append((edge[0], edges[edge]))

    print(graph_1)
    print(graph_2)
    print(graph_1 == graph_2)

    print('\na) A to K')
    costs, pred = dijkstra_sssp(graph_2, 'A')
    print('costs', costs)
    print('pred', pred)
    print('A to K:', find_path(pred, 'K'), costs['K'])

    print('\nb) H to D')
    costs, pred = dijkstra_sssp(graph_2, 'H')
    print('costs', costs)
    print('pred', pred)
    print('H to D:', find_path(pred, 'D'), costs['D'])

    print('\nc) B to I')
    costs, pred = dijkstra_sssp(graph_2, 'B')
    print('costs', costs)
    print('pred', pred)
    print('B to I:', find_path(pred, 'I'), costs['I'])

    print('\nd) I to C')
    costs, pred = dijkstra_sssp(graph_2, 'I')
    print('costs', costs)
    print('pred', pred)
    print('I to C:', find_path(pred, 'C'), costs['C'])

    print('\ne) J to H')
    costs, pred = dijkstra_sssp(graph_2, 'J')
    print('costs', costs)
    print('pred', pred)
    print('J to H:', find_path(pred, 'H'), costs['H'])


def dijkstra_sssp(graph, source_v):
    # Pseudocode
    '''
    Let distance of start vertex from start vertex = 0
    Let distance of all other vertices from start = infinity

    WHILE vertices remain unvisited
        Visit unvisited vertex with smallest known distance from start
        vertex (call this 'current vertex')
        FOR each unvisited neighbour of the current vertex
            Calculate the distance from start vertex
            IF the calculated distance of this vertex is less than the known distance
                Update the shortest distance to this vertex
                Update the previous vertex with the current vertex
            END IF
        NEXT unvisited neighbour
        Add the current vertex to the list of visited vertices
    END WHILE
    '''


    def add_entry(label, priority):
        'Add a new entry or update the priority of an existing entry.'

        if label in entry_finder:
            remove_entry(label)

        entry = [priority, label]
        entry_finder[label] = entry
        heapq.heappush(pq, entry)


    def remove_entry(label):
        'Mark an existing entry as REMOVED.'
        entry = entry_finder.pop(label)
        entry[-1] = REMOVED


    def pop_entry():
        'Remove and return the lowest priority entry.'

        while pq:
            priority, label = heapq.heappop(pq)
            if label != REMOVED:
                del entry_finder[label]
                return priority, label

        return None, None


    pq = []  # List of entries arranged in a heap (priority queue).
    entry_finder = {}  # Mapping of tasks to entries.
    REMOVED = '<removed-entry>'  # Placeholder for a removed entry.
    pred = {source_v: None}
    costs = {}

    # Initialize priority queue.
    for v in graph:
        if v == source_v:
            add_entry(source_v, 0)
        else:
            add_entry(v, math.inf)

    while pq:
        # pq[0] is the entry for the vertex with the current minimum path cost.
        d_u, u = pop_entry()

        # Note: vertex u precedes vertex v.
        if u is not None:
            for neighbor in graph[u]:
                if neighbor[0] not in costs:
                    v, w = neighbor
                    entry_v = entry_finder[v]
                    d_v = entry_v[0]

                    if d_v > d_u + w:
                        # Update entry for v in the priority queue.
                        add_entry(v, d_u + w)
                        pred[v] = u

            # Record shortest path to curr_v.
            costs[u] = d_u

    return costs, pred


def find_path(pred, destination):
    path = [destination]
    while path[0] is not None:
        path.insert(0, pred[path[0]])

    return ''.join(path[1:])


if __name__ == '__main__':
    main()
