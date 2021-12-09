import heapq
import math


def main():
    u_graph_a = {
       'A': [('B', 6), ('D', 1)],
        'B': [('A', 6), ('C', 5), ('D', 2), ('E', 2)],
        'C': [('B', 5), ('E', 5)],
        'D': [('A', 1), ('B', 2), ('E', 1)],
        'E': [('B', 2), ('C', 5), ('D', 1)]
    }

    d_graph_b = {
        'A': [('B', 2), ('C', 6), ('D', 7)],
        'B': [('D', 3), ('D', 6)],
        'C': [('E', 1)],
        'D': [('E', 5)],
        'E': []
    }

    d_graph_c = {
        '0': [('1', 2), ('2', 6), ('3', 7)],
        '1': [('3', 3), ('4', 6)],
        '2': [('4', 1)],
        '3': [('4', 5)],
        '4': []
    }

    costs, pred = shortest_path(d_graph_c, '0')
    print(costs)
    print(pred)


def shortest_path(graph, source_v):
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

    print('graph', graph)
    print('pq', pq)
    print('entry_finder', entry_finder)

    while pq:
        # pq[0] is the entry for the vertex with the current minimum path cost.
        d_u, u = pop_entry()

        # Note: vertex u precedes vertex v.
        if u is not None:
            for neighbor in graph[u]:
                if neighbor not in costs:
                    v, w = neighbor
                    entry_v = entry_finder[v]
                    d_v = entry_v[0]

                    print(d_v, d_u, d_u + w, d_v > d_u + w)
                    if d_v > d_u + w:
                        # Update entry for v in the priority queue.
                        add_entry(v, d_u + w)
                        pred[v] = u

            # Record shortest path to curr_v.
            costs[u] = d_u

    return costs, pred


if __name__ == '__main__':
    main()
