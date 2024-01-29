s = '9' * 58
while '9999' in s or '3333' in s:
    if '3333' in s:
        s = s.replace('3333', '99', 1)
    else:
        s = s.replace('9999', '33', 1)
print(s)