for n1 in range(20):
    for n2 in range(20):
        for n3 in range(20):
            s = '0' + '1' * n1 + '2' * n2 + '3' * n3
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30')
                s = s.replace('02', '3103')
                s = s.replace('03', '1201')
            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                print(n3)
                exit(0)