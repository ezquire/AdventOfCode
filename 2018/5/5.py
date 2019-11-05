from collections import Counter
import re

line = open("5.in", "r").read()
charlist = Counter(line.lower()).most_common()

def react(line, char):
    res = []
    for i in range(len(line)):
        if not res:
            res.append(line[i])
        elif char != None and (line[i] == char.lower() or line[i] == char.upper()):
            continue
        elif line[i] == res[-1]:
            res.append(line[i])
        elif line[i] == res[-1].upper() or line[i] == res[-1].lower():
            res.pop()
        else:
            res.append(line[i])
    return len(res)

def findShortest(line, count):
    min = float("inf")
    for char in charlist:
        length = react(line, char[0])
        min = length if length < min else min
    return min

# print(react(line, None))
print(findShortest(line, charlist))