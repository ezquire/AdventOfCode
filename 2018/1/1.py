fp = open("input1.txt", "r")
drift = 0
for line in iter(fp.readline, ''):
        drift += int(line)
print(drift)

def findDup():
    drift = 0
    seen = set([0])
    for _ in range(1000):
        fp = open("input1.txt", "r")
        for line in iter(fp.readline, ''):
            drift += int(line)
            if drift in seen:
                return drift
            seen.add(drift)
        fp = None
    return "No Duplicate Found"

print(findDup())
