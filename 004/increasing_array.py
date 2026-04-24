def solve():
    n = int(input())
    l = list(map(int, input().split()))

    amount = 0

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            diff = abs(l[i] - l[i - 1])
            l[i] += diff
            amount += diff
        
    print(amount)
    
if __name__ == '__main__':
    solve()
