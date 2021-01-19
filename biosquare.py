import numpy as np
import time
import random




def binarytodecimal(x):
    value = 0
    t = x.copy()
    for i in range(len(t)):
        digit = t.pop()
        if digit == 1:
            value = value + pow(2, i)
    return value


def roulettewheel(choices):
    maxi = sum(choices)
    decide = random.uniform(0, maxi)
    current = 0
    number = 0
    for choice in choices:
        current += choice
        if current > decide:
            return number
        number += 1


def createrandomnumber(x):
    tempr = []
    for j in range(x):
        temp2 = random.randint(0, 1)
        tempr.append(temp2)
    return tempr


def sign(x1, y1, x2, y2, x3, y3):
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)


def pointinsquare(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = sign(x0, y0, x1, y1, x2, y2)
    d2 = sign(x0, y0, x2, y2, x3, y3)
    d3 = sign(x0, y0, x3, y3, x4, y4)
    d4 = sign(x0, y0, x4, y4, x1, y1)

    has_neg1 = (d1 < 0) or (d3 < 0) or (d2 < 0) or (d4 < 0)
    has_pos1 = (d1 > 0) or (d3 > 0) or (d2 > 0) or (d4 > 0)
    return not (has_neg1 and has_pos1)


def determine4points(ly1, lx1, ly3, lx3):
    xmidpoint = (lx1 + lx3) / 2
    ymidpoint = (ly1 + ly3) / 2
    dx = abs(xmidpoint - lx1)
    dy = abs(ymidpoint - ly1)
    if lx1 < xmidpoint:
        lx2 = xmidpoint - dy
        lx4 = xmidpoint + dy
    else:
        lx2 = xmidpoint + dy
        lx4 = xmidpoint - dy
    if ly1 < ymidpoint:
        ly2 = ymidpoint + dx
        ly4 = ymidpoint - dx
    else:
        ly2 = ymidpoint - dx
        ly4 = ymidpoint + dx
    return [ly1, lx1], [ly2, lx2], [ly3, lx3], [ly4, lx4]


def countdots(y, x):
    global flg
    global counter1
    global counter2
    global square
    if flg == 1:
        return 0
    if pointinsquare(x, y, square[0][1], square[0][0],
                     square[1][1], square[1][0], square[2][1], square[2][0], square[3][1], square[3][0]):
        if virtual[y, x] == 0:

            virtual[y, x] = 1
            if int(lines[y][x]) == 1:
                counter1 += 1
                countdots(y + 1, x)
                countdots(y, x + 1)
                countdots(y - 1, x)
                countdots(y, x - 1)
            else:
                counter2 += 1
    if flg == 1:
        return 0
    return counter1
for i in range(500):
    start_time = time.time()
    #  READ
    filename = "inout/sqrn.txt"
    data = []
    with open(filename) as my_file:
        for line in my_file:
            data.append([list(map(float, x.split(', '))) for x in line.split(', ')])
    lines = np.array(data)
    maximum = [[0, [0, 0, 0, 0]]]
    #  CREATE INDIVIDUALS
    #try:
    #    indNum = int(input("Enter number of individuals: "))
    #except ValueError as err:
    #    print("error:")
    #    print(err)
    #    print("setting individuals number to default")
    indNum = 400
    #try:
    #    featNum = int(input("Enter number of features: "))
    #except ValueError as err:
    #    print("error:")
    #    print(err)
    #    print("setting features number to default")
    featNum = 6
    #  divider-1 = number of individuals/ (points of x's and y')
    divider = indNum / 4 + 1

    #print("Number of individuals:", indNum, "Number of features:", featNum)

    #  generate sequences of 0 and 1 for individuals
    individualsInBinary = []
    for i in range(int(indNum / 4)):
        i1 = createrandomnumber(featNum)
        i2 = createrandomnumber(featNum)
        i3 = createrandomnumber(featNum)
        i4 = createrandomnumber(featNum)
        individualsInBinary.append([[i1, i2], [i3, i4]])
    #  print(individualsInBinary)
    individualsInDecimal = []

    for x in individualsInBinary:
        x1 = binarytodecimal(x[0][0])
        x2 = binarytodecimal(x[0][1])
        x3 = binarytodecimal(x[1][0])
        x4 = binarytodecimal(x[1][1])
        individualsInDecimal.append([[x1, x2], [x3, x4]])

    statement = 0
    prev = maximum[0]
    repeats = 0
    #print('Dots, [[y1 x1], [y3, x3]], iteration')
    while statement < 5000:
        fieldsize = []
        #   print(len(individualsInDecimal))
        for i in individualsInDecimal:
            square = determine4points(i[0][0], i[0][1], i[1][0], i[1][1])

            #  Checking if any of points are counted outside img file
            brk = 0
            for cod in square:
                if cod[0] < 0 or cod[1] < 0 or cod[0] > (len(lines) - 1) or (cod[1] > len(lines[0]) - 1):
                    brk = 1
                    break
            if brk:
                brk = 0
                fieldsize.append(0)
                continue
            #  Check done

            midpoint = [int((i[0][0] + i[1][0]) / 2), int((i[0][1] + i[1][1]) / 2)]
            virtual = np.zeros((64, 64), dtype=int)
            flg = 0
            counter1 = 0
            counter2 = 0
            dotsum = countdots(midpoint[0], midpoint[1])
            if not counter2:
                fieldsize.append(dotsum)
            elif counter2/(counter2+counter1)>=0.95:
                fieldsize.append(dotsum*0.9)
                dotsum = 0
            elif counter2 / (counter2 + counter1) >= 0.90:
                fieldsize.append(dotsum * 0.8)
                dotsum = 0
            elif counter2/(counter2+counter1)>=0.85:
                fieldsize.append(dotsum*0.7)
                dotsum = 0
            else:
                fieldsize.append(0)
                dotsum = 0
            if dotsum == 0:
                continue
            if dotsum > maximum[0][0]:
                maximum = [[dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]]]
                #print(maximum, statement)
            elif dotsum == maximum[0][0]:
                maximum.append([dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]])
        fieldssrt = sorted(fieldsize)
        lambd = []
        mu = []
        #    print(len(fieldssrt))
        for i in fieldsize:
            z = 1
            for j in fieldssrt:
                if j == i:
                    key = z / divider
                    mu.append(key)  # or key
                    lambd.append(1 - key)  # 1-key
                    break
                else:
                    z += 1
        tmpsqares = individualsInBinary.copy()
        for i in range(len(tmpsqares)):
            for j in range(len(tmpsqares[i])):
                for k in range(len(tmpsqares[i][j])):
                    for l in range(len(tmpsqares[i][j][k])):
                        probs = lambd[i]
                        # print(probs)
                        rand = random.random()
                        if rand < probs:
                            mu2 = mu.copy()
                            mu2.pop(i)
                            tmpsqares2 = individualsInBinary.copy()
                            tmpsqares2.pop(i)
                            selected = roulettewheel(mu2)

                            tmpsqares[i][j][k][l] = tmpsqares2[selected][j][k][l]
                            if random.random() < 0.001:
                                tmpsqares[i][j][k][l] = abs(tmpsqares[i][j][k][l] - 1)
        individualsInBinary = tmpsqares.copy()
        individualsInDecimal = []
        for x in individualsInBinary:
            x1 = binarytodecimal(x[0][0])
            x2 = binarytodecimal(x[0][1])
            x3 = binarytodecimal(x[1][0])
            x4 = binarytodecimal(x[1][1])
            individualsInDecimal.append([[x1, x2], [x3, x4]])


        if prev == maximum[0]:
            repeats += 1
        else:
            repeats = 0
        if repeats == 2000:
            break
        else:
            prev = maximum[0]
        statement += 1

    for i in individualsInDecimal:
        square = determine4points(i[0][0], i[0][1], i[1][0], i[1][1])

        #  Checking if any of points are counted outside img file
        brk = 0
        for cod in square:
            if cod[0] < 0 or cod[1] < 0 or cod[0] > (len(lines) - 1) or (cod[1] > len(lines[0]) - 1):
                brk = 1
                break
        if brk:
            brk = 0
            continue
        #  Check done

        midpoint = [int((i[0][0] + i[1][0]) / 2), int((i[0][1] + i[1][1]) / 2)]
        virtual = np.zeros((64, 64), dtype=int)
        flg = 0
        counter1 = 0
        counter2 = 0
        dotsum = countdots(midpoint[0], midpoint[1])
        if counter2:
           dotsum = 0
        if dotsum == 0:
            continue
        if dotsum > maximum[0][0]:
            maximum = [[dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]]]
            #print(maximum)
        elif dotsum == maximum[0][0]:
            maximum.append([dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]])
    #print("Final:")
    #print('Length, dots, [[y1 x1], [y3, x3]]')
    print(len(maximum), " ", maximum[0])
    tm = int(time.time() - start_time)
    print("--- %s seconds ---" % tm)
    print("tikslumas: ", maximum[0][0]/92*100)
    with open("inout/rezstn.txt", "a") as myfile2:#92
        myfile2.write(str(tm) + " " + str(int(maximum[0][0]/92*100)) + "\n")
