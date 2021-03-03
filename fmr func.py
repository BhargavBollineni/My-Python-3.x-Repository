from functools import reduce

a = [2, 4, 3, 6, 7, 5, 7, 2, 9]
b = [1, 2, 5, 3, 4, 6, 8, 7, 5]



eve = list(filter(lambda n: n%2==0, a))
print(eve)

dob = list(map(lambda  n: n+2, b))
print(dob)

sum = reduce(lambda a, b: a+b, dob)
print(sum)

