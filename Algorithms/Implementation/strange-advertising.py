

liked = [2]
people = int(input().strip())
for i in range(people - 1):
    liked.append(int(round((liked[i] / 2), 1) * 3))
print (sum(liked))