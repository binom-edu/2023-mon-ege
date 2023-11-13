alf = 'абвгде'

ans = 0
for s1 in alf:
    for s2 in alf:
        for s3 in alf:
            for s4 in alf:
                for s5 in alf:
                    s = s1 + s2 + s3 + s4 + s5
                    if s.count('в') == 1 and (s1 == 'в' or s5 == 'в'):
                        ans += 1
print(ans)