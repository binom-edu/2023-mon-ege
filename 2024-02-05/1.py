# посчитать количество строк, в которых символ K встречается чаще, чем символ U

ans = 0

for s in open('1.txt'):
    if s.count('K') > s.count('U'):
        ans += 1

print(ans)