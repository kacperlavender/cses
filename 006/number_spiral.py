def solve():
    t = int(input())

    ans = []

    for _ in range(t):
        y, x = map(int, input().split())

        z = max(x, y)   

        if z % 2 == 0:
            if (y == z):
                ans.append(z * z - x + 1)
            else:
                ans.append((z - 1) * (z - 1) + y)

        else:
            if (x == z):
                ans.append(z * z - y + 1)
            else:
                ans.append((z - 1) * (z - 1) + x)

        t -= 1

    for i in ans:
        print(i)

if __name__ == '__main__':
    solve()
