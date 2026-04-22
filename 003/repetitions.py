def solve():
    string = input()
    l = [ch for ch in string]

    perm = 1
    temp = 1

    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            temp += 1

            if temp > perm: 
                perm = temp
        else:
            temp = 1

    print(perm)

if __name__ == '__main__':
    solve()