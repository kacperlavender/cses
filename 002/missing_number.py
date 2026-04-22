def solve():
    n = int(input())
    expected = n * (n+1) // 2

    l = list(map(int, input().split()))
    actual = sum(l)

    print(expected - actual)

if __name__ == '__main__':
    solve()