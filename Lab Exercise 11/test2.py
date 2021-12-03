def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


a = [20, 20, 10, 10, 10]
b = {}

for elem in a:
    if elem not in b:
        b[elem] = 1
    else:
        b[elem] += 1


numerator = factorial(len(a))
denominator = 1

for value in b.values():
    denominator *= factorial(value)

print(numerator, denominator)

def permute_rep(combis, unique_elems):




