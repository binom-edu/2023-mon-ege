def f(start, stop):
    if start == stop:
        return 1
    if start > stop:
        return 0
    return f(start * 2, stop) + f(start + 1, stop)

print(f(1, 10) * f(10, 20))