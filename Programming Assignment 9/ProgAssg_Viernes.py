import heapq
import math


def main():
    raw_upper_right = '10,10'
    raw_max_d = '4.1'
    raw_n = '10' # No. of planet/s.
    raw_planet_coords = '''9.92,0.83
        8.01,0.90
        9.48,2.53
        2.32,3.82
        5.57,6.14
        4.77,9.98
        8.33,4.33
        1.48,5.94
        7.11,6.48
        2.76,6.25'''

    upper_right = tuple(float(coord) for coord in raw_upper_right.split(','))
    max_d = float(raw_max_d)
    raw_n = int(raw_n)

    coords = {}
    ctr = 0

    for coord in raw_planet_coords.split('\n'):
        coords[str(ctr)] = tuple(float(coord) for coord in coord.strip().split(','))
        ctr += 1

    print('coords', coords)

    nearest_min, nearest_max = math.inf, math.inf
    start, end = '', ''

    for coord_name, coord in coords.items():
        r2_min = get_r2([0, 0], coord)
        r2_max = get_r2(upper_right, coord)

        if r2_min < nearest_min:
            nearest_min = r2_min
            start = coord_name

        if r2_max < nearest_max:
            nearest_max = r2_max
            end = coord_name

    print(start, end)

    costs, pred, coords_copy = search(coords, start, max_d)
    print('costs', costs)
    print('pred', pred)
    print('coords', coords)
    print('coords_copy', coords_copy)

    print(costs[end])
    print(get_path(coords_copy, pred, end))


def search(coords, start, max_d, coords_copy={}):
    pq = []  # List of entries arranged in a heap (priority queue).
    entry_finder = {}  # Mapping of tasks to entries.
    REMOVED = 'r'  # Placeholder for a removed entry.
    pred = {start: None}
    costs = {}

    # Initiate priority queue.
    for v in coords:
        if v == start:
            add_entry(start, 0, pq, entry_finder, REMOVED)
        else:
            add_entry(v, math.inf, pq, entry_finder, REMOVED)

    print('pq', pq)
    print('entry_finder', entry_finder)

    while pq:
        # pq[0] is the entry for the vertex with the current minimum path cost.
        d_u, u = pop_entry(pq, entry_finder, REMOVED)

        # Note: vertex u precedes vertex v.
        if u is not None:
            coord_u = coords.pop(u)
            coords_copy[u] = coord_u

            for coord_name_v, coord_v in coords.items():
                if coord_name_v not in costs:
                    w = get_r2(coord_u, coord_v) ** 0.5
                    if w <= max_d:
                        entry_v = entry_finder[coord_name_v]
                        d_v = entry_v[0]

                        if d_v > d_u + w:
                            # Update entry for v in the priority queue.
                            add_entry(coord_name_v, d_u + w, pq, entry_finder, REMOVED)
                            pred[coord_name_v] = u

            # Record shortest path to curr_v.
            costs[u] = d_u

    print('entry_finder', entry_finder)
    print('coords', coords)

    return costs, pred, coords_copy


def add_entry(label, priority, pq, entry_finder, REMOVED):
    'Add a new entry or update the priority of an existing entry.'

    if label in entry_finder:
        remove_entry(label, entry_finder, REMOVED)

    entry = [priority, label]
    entry_finder[label] = entry
    heapq.heappush(pq, entry)


def remove_entry(label, entry_finder, REMOVED):
    'Mark an existing entry as REMOVED.'

    entry = entry_finder.pop(label)
    entry[-1] = REMOVED


def pop_entry(pq, entry_finder, REMOVED):
    'Remove and return the lowest priority entry.'

    while pq:
        priority, label = heapq.heappop(pq)
        if label != REMOVED:
            del entry_finder[label]
            return priority, label

    return None, None


def get_path(coords, pred, end):
    path = [coords[end]]
    curr_v = pred[end]

    while curr_v is not None:
        path.insert(0, coords[curr_v])
        curr_v = pred[curr_v]

    return path


def get_r2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


if __name__ == '__main__':
    main()


# import heapq
# import math
#
#
# def main():
#     upper_right = tuple(float(coord) for coord in input().split(','))
#     max_d = float(input())
#     n = int(input())  # No. of planet/s.
#
#     coords = {}
#     nearest_min, nearest_max = math.inf, math.inf
#     start, end = '', ''
#
#     for i in range(n):
#         curr_coord = tuple(float(coord) for coord in input().split(','))
#         coords[str(i)] = curr_coord
#
#         r2_min = get_r2((0, 0), curr_coord)
#         r2_max = get_r2(upper_right, curr_coord)
#
#         if r2_min < nearest_min:
#             nearest_min = r2_min
#             start = str(i)
#
#         if r2_max < nearest_max:
#             nearest_max = r2_max
#             end = str(i)
#
#     costs, pred, coords_copy = search(coords, start, max_d)
#
#     print(costs[end])
#     print(get_path(coords_copy, pred, end))
#
#
# def search(coords, start, max_d, coords_copy={}):
#     pq = []  # List of entries arranged in a heap (priority queue).
#     entry_finder = {}  # Mapping of tasks to entries.
#     REMOVED = 'r'  # Placeholder for a removed entry.
#     pred = {start: None}
#     costs = {}
#
#     # Initiate priority queue.
#     for v in coords:
#         if v == start:
#             add_entry(start, 0, pq, entry_finder, REMOVED)
#         else:
#             add_entry(v, math.inf, pq, entry_finder, REMOVED)
#
#     while pq:
#         # pq[0] is the entry for the vertex with the current minimum path cost.
#         d_u, u = pop_entry(pq, entry_finder, REMOVED)
#
#         # Note: vertex u precedes vertex v.
#         if u is not None:
#             coord_u = coords.pop(u)
#             coords_copy[u] = coord_u
#
#             for coord_name_v, coord_v in coords.items():
#                 if coord_name_v not in costs:
#                     w = get_r2(coord_u, coord_v) ** 0.5
#                     if w <= max_d:
#                         entry_v = entry_finder[coord_name_v]
#                         d_v = entry_v[0]
#
#                         if d_v > d_u + w:
#                             # Update entry for v in the priority queue.
#                             add_entry(coord_name_v, d_u + w, pq, entry_finder, REMOVED)
#                             pred[coord_name_v] = u
#
#             # Record shortest path to curr_v.
#             costs[u] = d_u
#
#     return costs, pred, coords_copy
#
#
# def add_entry(label, priority, pq, entry_finder, REMOVED):
#     'Add a new entry or update the priority of an existing entry.'
#
#     if label in entry_finder:
#         remove_entry(label, entry_finder, REMOVED)
#
#     entry = [priority, label]
#     entry_finder[label] = entry
#     heapq.heappush(pq, entry)
#
#
# def remove_entry(label, entry_finder, REMOVED):
#     'Mark an existing entry as REMOVED.'
#
#     entry = entry_finder.pop(label)
#     entry[-1] = REMOVED
#
#
# def pop_entry(pq, entry_finder, REMOVED):
#     'Remove and return the lowest priority entry.'
#
#     while pq:
#         priority, label = heapq.heappop(pq)
#         if label != REMOVED:
#             del entry_finder[label]
#             return priority, label
#
#     return None, None
#
#
# def get_path(coords, pred, end):
#     path = [coords[end]]
#     curr_v = pred[end]
#
#     while curr_v is not None:
#         path.insert(0, coords[curr_v])
#         curr_v = pred[curr_v]
#
#     return path
#
#
# def get_r2(p1, p2):
#     return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
#
#
# if __name__ == '__main__':
#     main()
