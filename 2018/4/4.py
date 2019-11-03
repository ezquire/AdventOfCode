from collections import defaultdict

lines = open("4.in", "r").read().split('\n')
lines.sort()

def parseTime(line):
    words = line.split()
    time = words[1][:-1]
    return int(time.split(':')[1])

C = defaultdict(int)
CM = defaultdict(int)
guard = None
asleep = None
for line in lines:
    time = parseTime(line)
    if "begins shift" in line:
        guard = int(line.split()[3][1:])
        asleep = None
    elif "falls asleep" in line:
        asleep = time
    elif "wakes up" in line:
        for t in range(asleep, time):
            CM[(guard, t)] += 1
        C[guard] += (time - asleep)

def argmax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

def get_minute(d, guard):
    minute = None
    max_minute = float("-inf")
    for id, minutes in d.items():
        if id[0] == guard:
            if max_minute < d[id]:
                max_minute = d[id]
                minute = id[1]
    return minute


best_guard = max(C, key=C.get)
best_min = get_minute(CM, best_guard)

best_guard = max(CM, key=CM.get)
print(best_guard[0] * best_guard[1])
