


def organizingContainers(container):
    rows = list([0 for _ in range(len(container))])
    cols = list([0 for _ in range(len(container))])
    for i in range(len(container)):
        for j in range(len(container)):
            cols[j] += container[i][j]
            rows[i] += container[i][j]
    
    if sorted(rows) == sorted(cols):
        return "Possible"    
    else:
        return "Impossible"

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        container = []
        for i in range(n):
            container.append(list(map(int, input().rstrip().split())))
        print(organizingContainers(container))