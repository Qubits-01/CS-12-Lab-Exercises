# Partition the raw_time_logs according to each unique customer.
def partition_time_logs(time_logs):
    time_logs_seconds(time_logs)

    partitioned_time_logs = {}
    for time_log in time_logs:
        name = time_log[:time_log.find(' ')]
        time = int(time_log[time_log.find(' ') + 1:])

        if name in partitioned_time_logs:
            partitioned_time_logs[name].append(time)
        else:
            partitioned_time_logs[name] = [time]

    return partitioned_time_logs


# Computes the total time elapsed of a customer.
def compute_time_elapsed(time_data):
    if len(time_data) % 2 != 0:
        time_data.append(24 * 60 * 60)

    time_elapsed = 0
    for index in range(0, len(time_data), 2):
        time_elapsed += (time_data[index + 1] - time_data[index])

    return time_elapsed


# Computes the payable fee per time_elapsed.
def compute_fee(elapsed_time):
    hrs = elapsed_time / (60 * 60)
    excess_secs = elapsed_time % (60 * 60)

    if excess_secs == 0:
        additional_fee = 0
    elif excess_secs <= 30 * 60:
        additional_fee = 10
    else:
        additional_fee = 15

    fee = int(hrs) * 15 + additional_fee

    return fee


# Computes then total fee of all the customers.
def compute_total_fee(to_log_out, time_logs):
    total_fee = 0

    for name in to_log_out:
        time_data = time_logs[name]
        elapsed_time = compute_time_elapsed(time_data)

        total_fee += compute_fee(elapsed_time)

    return total_fee


# Sorts raw_time_logs by time value.
def sort_time_data(time_logs):
    for name in time_logs:
        time_logs[name].sort()


# Converts the time value of the time_logs into seconds.
def time_logs_seconds(time_logs):
    for index in range(len(time_logs)):
        time_log_parts = time_logs[index].split(' ')
        time_logs[index] = f'{time_log_parts[0]} {to_seconds(time_log_parts[1])}'


# Coverts the raw time value into seconds.
def to_seconds(time):
    # Indices' Legends:
    # 	0 : no. of hours
    # 	1 : no. of minutes
    # 	2 : no. of seconds

    time_parts = [int(time_part) for time_part in time.split(':')]

    h_to_s = time_parts[0] * 60 * 60
    m_to_d = time_parts[1] * 60
    s = time_parts[2]

    return h_to_s + m_to_d + s


if __name__ == '__main__':
    '''
    # Get the inputs.
    to_log_out = input().split()
    no_of_time_logs = int(input())

    raw_time_logs = []
    for _ in range(no_of_time_logs):
        raw_time_logs.append(input())
    '''

    to_log_out = 'Bob Claire Alex'.split()
    no_of_time_logs = '10'
    raw_time_logs = [
        'Bob 10:00:00',
        'Bob 11:00:00',
        'Spencer 8:00:00',
        'Spencer 7:00:00',
        'Claire 9:00:00',
        'Alex 8:00:00',
        'Alex 16:00:00',
        'Claire 21:30:00',
        'Kate 11:00:00',
        'James 12:32:59',
    ]

    time_logs = partition_time_logs(raw_time_logs)
    sort_time_data(time_logs)

    print(compute_total_fee(to_log_out, time_logs))

    print(time_logs)


# # Partition the raw_time_logs according to each unique customer.
# def partition_time_logs(time_logs):
#     time_logs_seconds(time_logs)
#
#     partitioned_time_logs = {}
#     for time_log in time_logs:
#         name = time_log[:time_log.find(' ')]
#         time = int(time_log[time_log.find(' ') + 1:])
#
#         if name in partitioned_time_logs:
#             partitioned_time_logs[name].append(time)
#         else:
#             partitioned_time_logs[name] = [time]
#
#     return partitioned_time_logs
#
#
# # Computes the total time elapsed of a customer.
# def compute_time_elapsed(time_data):
#     if len(time_data) % 2 != 0:
#         time_data.append(24 * 60 * 60)
#
#     time_elapsed = 0
#     for index in range(0, len(time_data), 2):
#         time_elapsed += (time_data[index + 1] - time_data[index])
#
#     return time_elapsed
#
#
# # Computes the payable fee per time_elapsed.
# def compute_fee(elapsed_time):
#     hrs = elapsed_time / (60 * 60)
#     excess_secs = elapsed_time % (60 * 60)
#
#     if excess_secs == 0:
#         additional_fee = 0
#     elif excess_secs <= 30 * 60:
#         additional_fee = 10
#     else:
#         additional_fee = 15
#
#     fee = int(hrs) * 15 + additional_fee
#
#     return fee
#
#
# # Computes then total fee of all the customers.
# def compute_total_fee(to_log_out, time_logs):
#     total_fee = 0
#
#     for name in to_log_out:
#         time_data = time_logs[name]
#         elapsed_time = compute_time_elapsed(time_data)
#
#         total_fee += compute_fee(elapsed_time)
#
#     return total_fee
#
#
# # Sorts raw_time_logs by time value.
# def sort_time_data(time_logs):
#     for name in time_logs:
#         time_logs[name].sort()
#
#
# # Converts the time value of the time_logs into seconds.
# def time_logs_seconds(time_logs):
#     for index in range(len(time_logs)):
#         time_log_parts = time_logs[index].split(' ')
#         time_logs[index] = f'{time_log_parts[0]} {to_seconds(time_log_parts[1])}'
#
#
# # Coverts the raw time value into seconds.
# def to_seconds(time):
#     # Indices' Legends:
#     # 	0 : no. of hours
#     # 	1 : no. of minutes
#     # 	2 : no. of seconds
#
#     time_parts = [int(time_part) for time_part in time.split(':')]
#
#     h_to_s = time_parts[0] * 60 * 60
#     m_to_d = time_parts[1] * 60
#     s = time_parts[2]
#
#     return h_to_s + m_to_d + s
#
#
# if __name__ == '__main__':
#     # Get the inputs.
#     to_log_out = input().split()
#     no_of_time_logs = int(input())
#
#     raw_time_logs = []
#     for _ in range(no_of_time_logs):
#         raw_time_logs.append(input())
#
#     time_logs = partition_time_logs(raw_time_logs)
#     sort_time_data(time_logs)
#
#     print(compute_total_fee(to_log_out, time_logs))
