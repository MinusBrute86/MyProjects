import random

values = {r: i for i, r in enumerate('123456789', 1)}
for r in 'TJQK':
    values[r] = 10
for r in 'A':
    values[r] = 11
print(values)
