# сумма цифр
n = int(input())
ans = 0

while n > 0:
    d = n % 10
    # что-то делаем с d
    ans += d
    n //= 10
print(ans)