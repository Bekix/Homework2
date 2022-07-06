import random

def examination(m):
    cell = input()
    while not cell.isdigit():
        cell = input('Please, enter number: ')
    while not check(m, cell):
        cell = input('This cell is already occupied or does not exist. Please enter another cell: ')
    return cell


def check(m, cell):
    for i in m:
        for j in i:
            if j != 'X' and j != 'O':
                if int(j) == int(cell):
                    return True
    return False

def Row_Column(m, symbl):
    f1 = False
    flag1 = -1
    f2 = False
    flag2 = -1
    for row in m:
        if row.count(symbl) >= 5:
            for i in range(len(row)):
                if row[i] == symbl and not f1:
                    f1 = True
                    flag1 = i
                elif row[i] == symbl and f1:
                    if i - flag1 == 4:
                        if symbl == 'X':
                            print("You lose!!!")
                        else:
                            print('CP lose!!')
                        exit()
                else:
                    f1 = False
                    flag1 = -1
    for i in range(10):
        for j in range(10):
            if m[j][i] == symbl and not f2:
                f2 = True
                flag2 = j
            elif m[j][i] == symbl and f2:
                if j - flag2 == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f2 = False
                flag2 = -1

def Diagonal(m, symbl):
    for j in range(5):
        f = False
        flag = -1
        h = j
        for i in range(10 - j):
            if m[i][h] == symbl and not f:
                f = True
                flag = i
            elif m[i][h] == symbl and f:
                if i - flag == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h += 1
    for j in range(5):
        f = False
        flag = -1
        h = j
        for i in range(10 - j):
            if m[h][i] == symbl and not f:
                f = True
                flag = i
            elif m[h][i] == symbl and f:
                if i - flag == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h += 1

def Reverse_Diagonal(m, symbl):
    for j in range(9, 3, -1):
        f = False
        flag = -1
        h = j
        for i in range(j):
            if m[i][h] == symbl and not f:
                f = True
                flag = i
            elif m[i][h] == symbl and f:
                if i - flag == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h -= 1
    for j in range(1, 6):
        f = False
        flag = -1
        h = j
        for i in range(9, j - 1, -1):
            if m[h][i] == symbl and not f:
                f = True
                flag = i
            elif m[h][i] == symbl and f:
                if abs(i - flag) == 4:
                    if symbl == 'X':
                        print("You lose!!!")
                    else:
                        print('CP lose!!')
                    exit()
            else:
                f = False
                flag = -1
            h += 1

def win(m):
    Row_Column(m, 'X')
    Row_Column(m, 'O')
    Diagonal(m, 'X')
    Diagonal(m, 'O')
    Reverse_Diagonal(m, 'X')
    Reverse_Diagonal(m, 'O')



def bot(m, cell):
    Options = []
    cell = int(cell)
    if cell - 10 > 0 and check(m, cell-10):
        Options.append(str(cell - 10))
    if cell + 10 < 100 and check(m, cell+10):
        Options.append(str(cell + 10))
    if cell % 10 != 9 and check(m, cell+1):
        Options.append(str(cell + 1))
    if cell % 10 != 0 and check(m, cell-1):
        Options.append(str(cell - 1))
    if cell % 10 != 0 and cell != cell % 10 and check(m, cell-11):
        Options.append(str(cell - 11))
    if cell % 10 != 9 and cell // 10 != 9 and check(m, cell+11):
        Options.append(str(cell + 11))

    random_index = random.randint(0, len(Options) - 1)
    x = Options[random_index]

    for i in range(10):
        for j in range(10):
            if m[i][j] == x:
                m[i][j] = 'O'
                return m


def player(m):
    cell = examination(m)
    for i in range(10):
        for j in range(10):
            if m[i][j] != 'X' and m[i][j] != 'O':
                if m[i][j] == cell or int(m[i][j]) == int(cell):
                    m[i][j] = 'X'
                    return m, cell


def game():
    matrix = []
    n = []
    count = 100
    for i in range(0, 9 + 1):
        n.append(str(i))
    matrix.append(n)
    n = []
    for i in range(10, 99 + 1):
        if i % 10 == 9:
            n.append(str(i))
            matrix.append(n)
            n = []
        else:
            n.append(str(i))
    while 'game' == 'game':
        for i in matrix:
            print(i)
        matrix, cell = player(matrix)
        win(matrix)
        matrix = bot(matrix, cell)
        win(matrix)
        count -= 1
        if count == 0:
            for i in matrix:
                print(i)
            print('Draw!')
            break

game()
