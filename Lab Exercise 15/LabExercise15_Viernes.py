import heapq
import math


def main():
    raw_wants = 'TV Shirt GPU'
    raw_n = '8'  # No. of possible barters.
    raw_barters = '''Paperclip A 100
        Paperclip B 20
        A C 21
        A B 100
        B C 1
        B TV 100
        B Shirt 1000
        C GPU 12'''

    wants = tuple(want for want in raw_wants.split())
    n = int(raw_n)

    graph = {}
    for barter_data in raw_barters.split('\n'):
        thing_a, thing_b, upgrade_cost = barter_data.strip().split()
        graph.setdefault(thing_a, []).append((thing_b, int(upgrade_cost)))
        graph.setdefault(thing_b, [])

    print(graph)

    costs, pred = dijkstra_sssp(graph, 'Paperclip')
    print('costs', costs)
    print('pred', pred)

    min_val = math.inf
    for want in wants:
        if want in costs:
            curr_cost = costs[want]
            if curr_cost < min_val:
                min_val = curr_cost

    print(min_val)


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

    print('pq', pq)
    print('entry_finder', entry_finder)

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


if __name__ == '__main__':
    main()


# import heapq
# import math
#
#
# def main():
#     wants = tuple(want for want in input().split())
#     n = int(input())
#
#     graph = {}
#     for i in range(n):
#         thing_a, thing_b, upgrade_cost = input().split()
#
#         graph.setdefault(thing_a, []).append((thing_b, int(upgrade_cost)))
#         graph.setdefault(thing_b, [])
#
#     costs, pred = dijkstra_sssp(graph, 'Paperclip')
#
#     min_val = math.inf
#     for want in wants:
#         if want in costs:
#             curr_cost = costs[want]
#             if curr_cost < min_val:
#                 min_val = curr_cost
#
#     print(min_val)
#
#
# def dijkstra_sssp(graph, source_v):
#     # Pseudocode
#     '''
#     Let distance of start vertex from start vertex = 0
#     Let distance of all other vertices from start = infinity
#
#     WHILE vertices remain unvisited
#         Visit unvisited vertex with smallest known distance from start
#         vertex (call this 'current vertex')
#         FOR each unvisited neighbour of the current vertex
#             Calculate the distance from start vertex
#             IF the calculated distance of this vertex is less than the known distance
#                 Update the shortest distance to this vertex
#                 Update the previous vertex with the current vertex
#             END IF
#         NEXT unvisited neighbour
#         Add the current vertex to the list of visited vertices
#     END WHILE
#     '''
#
#     def add_entry(label, priority):
#         'Add a new entry or update the priority of an existing entry.'
#
#         if label in entry_finder:
#             remove_entry(label)
#
#         entry = [priority, label]
#         entry_finder[label] = entry
#         heapq.heappush(pq, entry)
#
#     def remove_entry(label):
#         'Mark an existing entry as REMOVED.'
#         entry = entry_finder.pop(label)
#         entry[-1] = REMOVED
#
#     def pop_entry():
#         'Remove and return the lowest priority entry.'
#
#         while pq:
#             priority, label = heapq.heappop(pq)
#             if label != REMOVED:
#                 del entry_finder[label]
#                 return priority, label
#
#         return None, None
#
#     pq = []  # List of entries arranged in a heap (priority queue).
#     entry_finder = {}  # Mapping of tasks to entries.
#     REMOVED = '<removed-entry>'  # Placeholder for a removed entry.
#     pred = {source_v: None}
#     costs = {}
#
#     # Initialize priority queue.
#     for v in graph:
#         if v == source_v:
#             add_entry(source_v, 0)
#         else:
#             add_entry(v, math.inf)
#
#     while pq:
#         # pq[0] is the entry for the vertex with the current minimum path cost.
#         d_u, u = pop_entry()
#
#         # Note: vertex u precedes vertex v.
#         if u is not None:
#
#             for neighbor in graph[u]:
#                 if neighbor[0] not in costs:
#                     v, w = neighbor
#                     entry_v = entry_finder[v]
#                     d_v = entry_v[0]
#
#                     if d_v > d_u + w:
#                         # Update entry for v in the priority queue.
#                         add_entry(v, d_u + w)
#                         pred[v] = u
#
#             # Record shortest path to curr_v.
#             costs[u] = d_u
#
#     return costs, pred
#
#
# if __name__ == '__main__':
#     main()
