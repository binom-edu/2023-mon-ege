s = 'c:\\users\\admin\\Documents'
lst = s.split('\\')
for i in lst:
    print(i)

print(lst[2])
print('/'.join(lst))