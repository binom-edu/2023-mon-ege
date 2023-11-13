def f1():
    return (x or not y) == (z <= w)

def f2():
    return (not x == y) and (z <= w)

print('x y z w 1 2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, int(f1()), int(f2()))