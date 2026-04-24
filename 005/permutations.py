def solve():
    n = int(input())

    if n == 1:
        print(1)
        return

    if n <= 3:
        print('NO SOLUTION')
        return

    l = [x for x in range(1, n + 1)]

    even = [x for x in l if x % 2 == 0]
    odd = [x for x in l if x % 2 != 0]

    print(*(even + odd))

if __name__ == '__main__':
    solve()