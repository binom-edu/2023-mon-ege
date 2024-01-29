s = '2' * 400
ans = 0
while '222' in s or '333' in s:
    if '333' in s:
        s = s.replace('333', '2', 1)
    else:
        s = s.replace('222', '3', 1)
        ans += 3
print(ans)