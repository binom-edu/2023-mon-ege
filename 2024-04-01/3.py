def getDivisors(n):
    ans = set()
    for d in range(2, n):
        if n % d == 0:
            ans.add(d)
            ans.add(n // d)
        if d ** 2 >= n:
            break
    return ans

def m(n):
    divs = getDivisors(n)
    if divs:
        return sum(divs) // len(divs)
    return 0

n = 550000
cnt = 0
while cnt < 5:
    if m(n) % 31 == 13:
        print(n, m(n))
        cnt += 1
    n += 1