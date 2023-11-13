# составляем 4-буквенные слова из букв b, i, n, o, m,
# причем каждая буква может встречаться любое количество раз или не
# встречаться совсем

alf = sorted('binom')
for s1 in alf:
    for s2 in alf:
        for s3 in alf:
            for s4 in alf:
                s = s1 + s2 + s3 + s4
                print(s)
