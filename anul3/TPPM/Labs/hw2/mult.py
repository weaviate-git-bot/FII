import random

times = 0
while True:
    x = random.random() #/1000000
    y = random.random() #/1000000
    z = random.random() #/1000000
    times += 1
    if (x * y) * z != x * (y * z):
        print('Neq', x,y,z)
        break

print('Iterations: ', times)