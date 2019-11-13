from collections import defaultdict
import heapq

# Edge
E = defaultdict(list)
# In-degree
D = defaultdict(int)

def makeGraph(E, D):
    for line in open('7.in'):
        words = line.split()
        x = words[1]
        y = words[7]
        E[x].append(y)
        D[y] += 1
        if x not in D:
            D[x] = 0

def makeQueue(Q):
    for x in E:
        if D[x] == 0:
            heapq.heappush(Q, x)

# def do_work(EV, Q, t):
#     while len(EV) < 5 and Q:
#         x = heapq.heappop(Q)
#         heapq.heappush(EV, (t+61+ord(x)-ord('A'), x))

# def findTime():
#     t = 0     # Time
#     EV = []   # Events
#     Q = []    # Work queue
#     makeQueue(Q)
#     do_work(EV, Q, t)
#     while EV or Q:
#         t, x = heapq.heappop(EV)
#         for y in E[x]:
#             D[y] -= 1
#             if D[y] == 0:
#                 heapq.heappush(Q, y)
#         do_work(EV, Q, t)
#     return t

def sort():
    Q = []
    makeQueue(Q)
    ans = ""
    while Q:
        x = heapq.heappop(Q)
        ans += x
        for y in E[x]:
            D[y] -= 1
            if D[y] == 0:
                heapq.heappush(Q, y)
    return ans

makeGraph(E, D)
# print(findTime())
print(sort())