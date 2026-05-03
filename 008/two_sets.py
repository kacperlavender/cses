n = int(input())

if n % 4 == 2 or n % 4 == 1:
    print("NO")
    exit()

goal = n * (n + 1) // 4

first = list()
second = list()

for i in range(n, 0, -1):
    if i < goal or i == goal:
        first.append(i)
        goal -= i

    else:
        second.append(i)

print("YES")

print(len(first))
print(*(first))

print(len(second))
print(*(second))
