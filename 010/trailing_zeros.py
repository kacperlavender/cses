import math

n = int(input())

fact = math.factorial(n)

t = 0

while fact % 10 == 0:
    t = t + 1
    fact = fact // 10

print(t)
