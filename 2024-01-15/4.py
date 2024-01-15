# сумма цифр числа
def f(n):
    if n == 0:
        return 0
    return n % 10 + f(n // 10)

print(f(int(input())))