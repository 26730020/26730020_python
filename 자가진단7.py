lst = []
while True:
    n = int(input())
    if n == 0:
        break
    lst.append(n)

print(*lst[1::2])
