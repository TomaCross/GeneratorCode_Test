import random
while True:
    a = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'A', 'B', 'C', '-', '$']
    random.shuffle(a)
    print(''.join(a))