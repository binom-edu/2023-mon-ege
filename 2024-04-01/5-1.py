# 1?5719*6
import fnmatch

# def isValid(n):
#     s = str(n)
#     return s[0] == '1' and s[2:6] == '5719' and s[-1] == '6'

for x in range(0, 10 ** 10, 2023):
    s = str(x)
    if fnmatch.fnmatch(s, '1?5719*6'):
        print(x, x // 2023)