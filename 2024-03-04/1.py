def r(x, y):
    return (x ** 2 + y ** 2) ** 0.5

points = [(0, 1), (5, 5), (7, -3)]

max_d = 0
i_max = 0

for i, point in enumerate(points):
    x, y = point
    if r(x, y) > max_d:
        max_d = r(x, y)
        i_max = i
print(i_max)