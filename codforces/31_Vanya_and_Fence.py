n, h = map(int, input().split())
persons = input().split()[:n]
road_width = 0
for i in persons:
    if int(i) > h:
        road_width += 2
    else:
        road_width += 1
print(road_width)
