

n = int(input().strip())

for i in range(n):
    line = ""
    for j in range(n):
        if j < ((n - 1) - i):
            line = line + " "
        else:
            line = line + "#"
    print (line)