def main():
    n = 7  # No. of IP address/es.
    ip_addresses = [
        '192.168.0.1',
        '192.168.0.2',
        '192.168.0.3',
        '192.168.0.255',
        '192.168.1.1',
        '192.168.1.2',
        '192.168.1.255'
    ]

    graph = {}
    ctr = 0

    for ip1 in ip_addresses:
        ctr += 1

        for ip2 in ip_addresses[ctr:]:
            segments1, segments2 = ip1.split('.'), ip2.split('.')

            if compare(segments1[:2], segments2[:2]):
                if compare(segments1[:3], segments2[:3]) \
                or (is_255(segments1[3]) and is_255(segments2[3])):
                    graph.setdefault(ip1, []).append(ip2)
                    graph.setdefault(ip2, []).append(ip1)
            else:
                break

        print(f'{ip1} : {sorted(graph.setdefault(ip1, []))}')


def compare(ip1_segments, ip2_segments):
    return True if ip1_segments == ip2_segments else False


def is_255(ip_last):
    return True if ip_last == '255' else False


if __name__ == '__main__':
    main()


# def main():
#     n = int(input())  # No. of IP address/es.
#     ip_addresses = []
#
#     for _ in range(n):
#         ip_addresses.append(input())
#
#     graph = {}
#     ctr = 0
#
#     for ip1 in ip_addresses:
#         ctr += 1
#
#         for ip2 in ip_addresses[ctr:]:
#             segments1, segments2 = ip1.split('.'), ip2.split('.')
#
#             if compare(segments1[:2], segments2[:2]):
#                 if compare(segments1[:3], segments2[:3]) \
#                         or (is_255(segments1[3]) and is_255(segments2[3])):
#                     if ip1 in graph:
#                         graph[ip1].append(ip2)
#                     else:
#                         graph[ip1] = [ip2]
#
#                     if ip2 in graph:
#                         graph[ip2].append(ip1)
#                     else:
#                         graph[ip2] = [ip1]
#             else:
#                 break
#
#         print(f'{ip1} : {sorted(graph.setdefault(ip1, []))}')
#
#
# def compare(ip1_segments, ip2_segments):
#     return True if ip1_segments == ip2_segments else False
#
#
# def is_255(ip_last):
#     return True if ip_last == '255' else False
#
#
# if __name__ == '__main__':
#     main()
