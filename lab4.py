from functools import reduce
def sum_neshet_index(numbers):
    return reduce(lambda acc, x: acc + x[1]**2 if x[0] % 2 != 0 else acc, enumerate(numbers), 0)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_neshet_index(numbers)
print(result)
