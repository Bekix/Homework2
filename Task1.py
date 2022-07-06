import itertools
def postman(points):
    points.append(points[0])
    points_changed = list(itertools.permutations(points))
    Options = []
    mn = 10**10

    for i in points_changed:
        if i[0] == i[-1] == points[0] and Options.count(i) == 0:
            Options.append(i)

    for i in Options:
        summa = 0
        string = ''
        count = 1
        for sweetie in range(len(i) - 1):
            if count == 1:
                string += str(i[sweetie])
                count += 1
            summa += ((i[sweetie + 1][0] - i[sweetie][0]) ** 2 + (i[sweetie + 1][1] - i[sweetie][1]) ** 2) ** 0.5
            string += '->' + str(i[sweetie+1]) + '[' + str(summa) + ']'
        if summa < mn:
            mn = summa
            answer = string
    return answer



print(postman([(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]))