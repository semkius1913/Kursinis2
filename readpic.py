
def prefcolor(r, g, b):
    if (r == b'\x00') and (g == b'\x00') and(b == b'\x00'):
        return 1
    else:
        return 0


location = "inout/sqrn.bmp"

colR = []
colG = []
colB = []

with open(location, "rb") as myfile:
    typfile = myfile.read(2)
    print(typfile)
    if (typfile != b'BM'):
        raise ValueError("{}:not a bmp".format(location))
#  2 first bytes are already taken (mostly it is translated to 'BM'
#  now take 4 bytes for size of file (36 in hex translates to char '6' but it means 54 in decimal. so 54bytes
    print("size: ")
    print(myfile.read(4))
#  reserve
    print(myfile.read(4))
    print("offset (should be 6): ")
#  where the colors start
    print(myfile.read(4))
    print("size of header (should be '(' ): ")
    print(myfile.read(4))
    print("width: ")
    print(myfile.read(4))
    print("length: ")
    print(myfile.read(4))
    print(myfile.read(2))
    print("bits per pixel" )
    print(myfile.read(2))
    print("compression: ")
    print(myfile.read(4))
    print(myfile.read(20))
# should start reading pixels, 3bytes per pix
    while True:
        colbyte = myfile.read(1)
        if not colbyte:
            break
        colB.append(colbyte)
        colG.append(myfile.read(1))
        colR.append(myfile.read(1))

print(colR[:10])
print(colG[:10])
print(colB[:10])

lst = []
for i in range(64):
    lst2 = []
    for j in range(64):
        r = colR.pop()
        g = colG.pop()
        b = colB.pop()
        lst2.append(prefcolor(r,g,b))
    lst2.reverse()
    lst.append(lst2)

location2 = "inout/sqrn.txt"
with open(location2, "w+") as myfile2:
    for i in lst[:-1]:
        myfile2.write(str(i)[1:-1] + "\n")
#  not to have newline symbol in the end of file
    myfile2.write(str(lst[-1])[1:-1])
