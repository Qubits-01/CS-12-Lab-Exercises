# no_of_test_cases = 1
#
# for _ in range(no_of_test_cases):
#     # Get the input data.
#     # Index legend:
#     #   0 to 2 : Dimensions of the luggage (assumed as rectangular).
#     #   3 : Weight of the luggage.
#     #   4 : Distance from origin to destination.
#     raw_input_data = '120.13 111.11 94.30 5.58 24.1'
#     input_data = [float(data) for data in raw_input_data.strip().split()]
#     print(input_data)
#
#     # Compute for the volume of the luggage.
#     volume = 1.00
#     for index in range(3):
#         volume *= input_data[index]
#     print(volume)
#
#     # Compute for the shipping fee.
#     shipping_fee = ((volume * 0.11) + (input_data[3] * 1.2) + (input_data[4] * 2.1)) / 150
#     print(shipping_fee)
#
#     # Identify which courier or pick-up.
#     if 0 <= shipping_fee <= 256:
#         print('DeliBeary')
#     elif 256 < shipping_fee <= 420:
#         print('StarShips')
#     elif 420 < shipping_fee <= 624:
#         print('PawDala')
#     elif 624 < shipping_fee <= 1000:
#         print('LBeeC')
#     else:
#         print('Pick-up')

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    # Get the input data.
    # Index legend:
    #   0 to 2 : Dimensions of the luggage (assumed as rectangular).
    #   3 : Weight of the luggage.
    #   4 : Distance from origin to destination.
    input_data = [float(data) for data in input().strip().split()]

    # Compute for the volume of the luggage.
    volume = 1.00
    for index in range(3):
        volume *= input_data[index]

    # Compute for the shipping fee.
    shipping_fee = ((volume * 0.11) + (input_data[3] * 1.2) + (input_data[4] * 2.1)) / 150

    # Identify which courier or pick-up.
    if 0 <= shipping_fee <= 256:
        print('DeliBeary')
    elif 256 < shipping_fee <= 420:
        print('StarShips')
    elif 420 < shipping_fee <= 624:
        print('PawDala')
    elif 624 < shipping_fee <= 1000:
        print('LBeeC')
    else:
        print('Pick-up')
