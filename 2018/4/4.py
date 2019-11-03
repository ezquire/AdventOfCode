# class Guard:
#     def __init__(self, date, time, id):
#         self.date = date
#         self.time = time
#         self.id = id

lines = open("4.in", "r").read().split('\n')
lines.sort()

for line in lines:
    print(line)
