import re

board = [[0]*1000 for _ in range(1000)]

fp = open("input3.txt", "r")

def processLine(line):
    rect_re = re.compile("\\d+")
    rect = rect_re.findall(line)
    return rect

rects = [] 
for line in iter(fp.readline, ''):
    rects.append(processLine(line))

total = 0

for rect in rects:
    num = int(rect[0])
    x = int(rect[1])
    y = int(rect[2])
    w = int(rect[3])
    h = int(rect[4])
    valid_id = True
    for i in range(x, x + w):
        for j in range(y, y + h):
            if board[i][j] == 0:
                board[i][j] = num
            elif board[i][j] > 0:
                valid_id = False
                board[i][j] = -1
                total += 1
            elif board[i][j] == -1:
                valid_id = False
    if valid_id: print(num)

print(total)