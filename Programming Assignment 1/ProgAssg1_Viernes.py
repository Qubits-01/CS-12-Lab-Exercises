# # Core Function/s ------------------------------------------------------------
# # Retrieve the voucher codes while removing
# # subsequent repeated voucher codes.
# def retrieve_vouchers():
#     no_of_vouchers = int(input())
#     vouchers = []
#     voucher_codes = []
#
#     for _ in range(no_of_vouchers):
#         temp_voucher = input().split(',')
#         fix_voucher_data_types(temp_voucher)
#
#         if voucher_codes.count(temp_voucher[0]) == 0:
#             vouchers.append(temp_voucher)
#             voucher_codes.append(temp_voucher[0])
#
#     return vouchers
#
#
# def retrieve_carts():
#     no_of_carts = int(input())
#     carts = []
#
#     for _ in range(no_of_carts):
#         cart_prices = [float(cart_price) for cart_price in input().split(',')]
#         carts.append(cart_prices)
#
#     return carts
#
#
# def get_cart_metadata(cart):
#     # Indices legends for cart_metadata:
#     #   0 : total_amount
#     #   1 : no_of_cart_items
#     cart_metadata = []
#     total_amount = 0.00
#
#     for cart_price in cart:
#         total_amount += cart_price
#
#     cart_metadata.extend([total_amount, len(cart)])
#
#     return cart_metadata
#
#
# def is_passing(voucher, cart):
#     # Return True if no_of_cart_items >= min_items and
#     # total_amount >= min_amount.
#     if (cart[1] >= voucher[2]) and (cart[0] >= voucher[3]):
#         return True
#     else:
#         return False
# # End of Core Functions ------------------------------------------------------
#
#
# # Helper Functions -----------------------------------------------------------
# def fix_voucher_data_types(voucher):
#     voucher[0] = voucher[0].upper()
#     voucher[1] = float(voucher[1])
#     voucher[2] = int(voucher[2])
#     voucher[3] = float(voucher[3])
#
#
# # Round up a decimal number into the nearest
# # whole number.
# def round_up(decimal):
#     rounded_up_no = int(decimal)
#
#     if decimal - rounded_up_no != 0:
#         rounded_up_no += 1
#
#     return rounded_up_no
#
#
# def pick_first_best_discount(cart_discounts):
#     # Start from the end of the cart_discounts list.
#     for index in range(len(cart_discounts)-1, 0, -1):
#         if cart_discounts[index][0] > cart_discounts[index-1][0]:
#             return cart_discounts[index]
#
#         if cart_discounts[index][0] == cart_discounts[index-1][0]:
#             continue
#
#     return cart_discounts[0]
# # End of Helper Function/s ---------------------------------------------------
#
#
# if __name__ == '__main__':
#     # vouchers = retrieve_vouchers()
#     # carts = retrieve_carts()
#
#     no_of_vouchers = 3
#     no_of_carts = 5
#
#     vouchers = [
#         ['LMN', 5.0, 2, 300.0],
#         ['XYZ', 10.0, 2, 400.0],
#         ['ABC', 20.0, 3, 1000.0]
#     ]
#
#     carts = [
#         [500.0, 100.0, 300.0],
#         [1200.0],
#         [1000.0, 3200.0, 100.0],
#         [100.0, 100.0, 100.0],
#         [200.0, 200.0]
#     ]
#
#     # Get the total amount and no. of cart_items.
#     carts_metadata = []
#     for cart in carts:
#         carts_metadata.append(get_cart_metadata(cart))
#
#     # Try all vouchers in each cart.
#     for cart in carts_metadata:
#         cart_discounts = []
#
#         for voucher in vouchers:
#             if is_passing(voucher, cart):
#                 discount = round_up(cart[0] * voucher[1] * 0.01)
#                 cart_discounts.append([discount, voucher[0]])
#
#         if len(cart_discounts) > 0:
#             cart_discounts.sort(key=lambda cart: (cart[0], cart[1]))
#             first_best_discount = pick_first_best_discount(cart_discounts)
#
#             print(f'{int(cart[0] - first_best_discount[0])},{first_best_discount[1]}')
#         else:
#             print(int(cart[0]))


# Core Function/s ------------------------------------------------------------
# Retrieve the voucher codes while removing
# subsequent repeated voucher codes.
def retrieve_vouchers():
    no_of_vouchers = int(input())
    vouchers = []
    voucher_codes = []

    for _ in range(no_of_vouchers):
        temp_voucher = input().split(',')
        fix_voucher_data_types(temp_voucher)

        if voucher_codes.count(temp_voucher[0]) == 0:
            vouchers.append(temp_voucher)
            voucher_codes.append(temp_voucher[0])

    return vouchers


def retrieve_carts():
    no_of_carts = int(input())
    carts = []

    for _ in range(no_of_carts):
        cart_prices = [float(cart_price) for cart_price in input().split(',')]
        carts.append(cart_prices)

    return carts


def get_cart_metadata(cart):
    # Indices legends for cart_metadata:
    #   0 : total_amount
    #   1 : no_of_cart_items
    cart_metadata = []
    total_amount = 0.00

    for cart_price in cart:
        total_amount += cart_price

    cart_metadata.extend([total_amount, len(cart)])

    return cart_metadata


def is_passing(voucher, cart):
    # Return True if no_of_cart_items >= min_items and
    # total_amount >= min_amount.
    if (cart[1] >= voucher[2]) and (cart[0] >= voucher[3]):
        return True
    else:
        return False
# End of Core Functions ------------------------------------------------------


# Helper Functions -----------------------------------------------------------
def fix_voucher_data_types(voucher):
    voucher[0] = voucher[0].upper()
    voucher[1] = float(voucher[1])
    voucher[2] = int(voucher[2])
    voucher[3] = float(voucher[3])


# Round up a decimal number into the nearest
# whole number.
def round_up(decimal):
    rounded_up_no = int(decimal)

    if decimal - rounded_up_no != 0:
        rounded_up_no += 1

    return rounded_up_no


def pick_first_best_discount(cart_discounts):
    # Start from the end of the cart_discounts list.
    for index in range(len(cart_discounts)-1, 0, -1):
        if cart_discounts[index][0] > cart_discounts[index-1][0]:
            return cart_discounts[index]

        if cart_discounts[index][0] == cart_discounts[index-1][0]:
            continue

    return cart_discounts[0]
# End of Helper Function/s ---------------------------------------------------


if __name__ == '__main__':
    vouchers = retrieve_vouchers()
    carts = retrieve_carts()

    # Get the total amount and no. of cart_items.
    carts_metadata = []
    for cart in carts:
        carts_metadata.append(get_cart_metadata(cart))

    # Try all vouchers in each cart.
    for cart in carts_metadata:
        cart_discounts = []

        for voucher in vouchers:
            if is_passing(voucher, cart):
                discount = round_up(cart[0] * voucher[1] * 0.01)
                cart_discounts.append([discount, voucher[0]])

        if len(cart_discounts) > 0:
            cart_discounts.sort(key=lambda cart: (cart[0], cart[1]))
            first_best_discount = pick_first_best_discount(cart_discounts)

            print(f'{int(cart[0] - first_best_discount[0])},{first_best_discount[1]}')
        else:
            print(int(cart[0]))
