def f():
    return (int(x or w) <= int(w or not y)) == (not z or y)

print('x y z w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not f():
                    print(x, y, z, w)