def f(s):
    if s >= 50:
        return ['-', 0]
    moves = [f(s + 2), f(s * 3)]
    win = []
    lose = []
    for move in moves:
        if move[0] == '-':
            win.append(move[1])
        else:
            lose.append(move[1])
    if win:
        return ['+', min(win) + 1]
    else:
        return ['-', max(lose)]
    
for s in  range(1, 50):
    print(s, *f(s))