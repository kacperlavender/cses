def solve():
    n = int(input())
    l = list(map(int, input().split()))

    amount = 0

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            while l[i] < l[i - 1]:
                l[i] = l[i] + 1
                amount += 1
        
    print(amount)
    
if __name__ == '__main__':
    solve()
