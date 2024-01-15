def numberOfDigits(n):
    ans = 0
    while n > 0:
        ans += 1
        n //= 10
    return ans

def check(n):
    m = n
    k = numberOfDigits(n)
    ans = 0
    while n > 0:
        ans += (n % 10) ** k
        n //= 10
    return m == ans

for n in range(1000):
    if check(n):
        print(n)