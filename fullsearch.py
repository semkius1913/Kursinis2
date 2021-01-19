import numpy as np
import time

start_time = time.time()


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
    global counter
    global square
    if flg == 1:
        return 0
    if pointinsquare(x, y, square[0][1], square[0][0],
                     square[1][1], square[1][0], square[2][1], square[2][0], square[3][1], square[3][0]):
        if virtual[y, x] == 0:

            virtual[y, x] = 1
            if int(lines[y][x]) == 1:
                counter = counter + 1
                countdots(y+1, x)
                countdots(y, x+1)
                countdots(y-1, x)
                countdots(y, x-1)
            else:
                flg = 1
                return 0

    if flg == 1:
        return 0
    return counter


print('Dots, [[y1 x1], [y3, x3]], iteration')
filename = "inout/sqrn.txt"
data = []
with open(filename) as my_file:
    for line in my_file:
        data.append([list(map(float, x.split(', '))) for x in line.split(', ')])
lines = np.array(data)
maximum = [[25, [0, 0, 0, 0]]]
for y in range(len(lines)):
    for x in range(len(lines[0])):
        for yy in range(len(lines)):
            for xx in range(len(lines[0])):
                square = determine4points(y, x, yy, xx)
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

                midpoint = [int((y+yy)/2), int((x + xx)/2)]
                virtual = np.zeros((64, 64), dtype=int)
                flg = 0
                counter = 0
                dotsum = countdots(midpoint[0], midpoint[1])
                if dotsum == 0:
                    continue
                if dotsum > maximum[0][0]:
                    maximum = [[dotsum, square]]
                    print(maximum,)
                elif dotsum == maximum[0][0]:
                    maximum.append([dotsum, [y, x, yy, xx]])

print(maximum)
print("--- %s seconds ---" % (time.time() - start_time))
