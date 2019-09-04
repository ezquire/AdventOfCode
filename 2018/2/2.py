from collections import Counter

fp = open("input2.txt", "r")

def checksum(fp):
    two = 0
    three = 0
    for line in iter(fp.readline, ''):
        counts = Counter(line)
        seen_two = False
        seen_three = False
        for key in counts.keys():
            if counts[key] == 2 and not seen_two:
                two += 1
                seen_two = True
            elif counts[key] == 3 and not seen_three:
                three += 1
                seen_three = True
    return two * three

print(checksum(fp))

def findCommon(ids):
    for id1 in ids:
        for id2 in ids:
            similar = differsByOne(id1, id2)
            if similar != None: 
                return similar

def differsByOne(line, line2):
    similar = ""
    if len(line) != len(line2): 
        return None
    difference = 0
    for i in range(len(line)):
        if line[i] != line2[i]:
            difference += 1
        else:        
            similar += line[i]
    if difference != 1: 
        return None
    else:
        return similar
    return None

ids = []

for line in iter(fp.readline, ''):
    ids.append(line)

print(findCommon(ids))