def solve():
    n = int(input())
    l = [n]
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
            l.append(n)

        else:
            n = 3 * n + 1
            l.append(n)

    print(' '.join(map(str, l)))

if __name__ == '__main__':
    solve()