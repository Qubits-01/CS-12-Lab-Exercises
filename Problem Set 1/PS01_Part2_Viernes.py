# 2.3.
def F(a, b):
    # Base cases.
    if a == 0 or b == 0:
        return 0

    if a == 1 or b == 1:
        return 1

    # Recursive step.
    return G(a-1, b-1) + F(a, b-1) * a


def G(a, b):
    # Base cases.
    if a == 0 or b == 0:
        return 1

    if a == 1 or b == 1:
        return 0

    # Recursive step.
    return F(a-1, b-1) + G(a-1, b) * b


print(G(3, 4))
print(F(5, 5))
print(G(12, 5))
print(F(9, 11))
print(G(9, 11))


# # 2.4.a.
# def P(x, y):
#     # Base cases.
#     if x == 0:
#         return 0
#
#     if y == 0:
#         return 1
#
#     # Recursive step.
#     return P(x-1, y-1) + P(x-1, y)
#
#
# # 2.4.b.
# def G(x, y):
#     # Base case.
#     # Means y is a factor of x or x is divisible by y.
#     if x % y == 0:
#         return y
#
#     # Recursive step.
#     return G(y, x%y)
#
#
# print('4.a.')
# print(P(5, 6))
# print(P(9, 1))
# print(P(10, 10))
#
# print('\n4.b.')
# print(G(82, 74))
# print(G(73, 85))
