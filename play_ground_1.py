import heapq
import math


def dijkstra(G, S):
    pq = []
    entry_finder = {}
    costs = {}
    pred = {S: None}  # init pred
    REMOVED = 'removed'

    def add_entry(label, priority):
        if label in entry_finder:
            remove_entry(label)
        entry = [priority, label]
        entry_finder[label] = entry
        heapq.heappush(pq, entry)

    def remove_entry(label):
        entry = entry_finder.pop(label)
        entry[-1] = REMOVED

    def pop_entry():
        while pq:
            priority, label = heapq.heappop(pq)
            if label != REMOVED:
                del entry_finder[label]
                return priority, label
        return None, None

    for v in G:  # init priority queue
        if v == S:
            add_entry(S, 0)
        else:
            add_entry(v, math.inf)
    while pq:
        # pq[0] is the entry for the vertex with the current minimum path cost
        d_u, u = pop_entry()
        if u is not None and u != REMOVED:
            costs[u] = d_u  # record shortest path to u
            for e in G[u]:
                v, w = e
                entry_v = entry_finder[v]
                d_v = entry_v[0]
                if d_v > d_u + w:
                    add_entry(v, d_u + w)  # update entry for v in priority queue
                    pred[v] = u
    return costs, pred


G = {
    '0': [('1', 2), ('2', 6), ('3', 7)],
    '1': [('3', 3), ('4', 6)],
    '2': [('4', 1)],
    '3': [('4', 5)],
    '4': []
}

d_graph_a = {}

costs, pred = dijkstra(G, '0')
print(costs)
print(pred)

