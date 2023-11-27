# перевод в систему счисления с основанием q
n = int(input())
q = int(input())

while n > 0:
    d = n % q
    # что-то делаем с d
    print(d)
    n //= q