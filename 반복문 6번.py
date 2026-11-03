max_val = 0

while True:
    num = int(input())
    if num == 0:
        break
    max_val = max(max_val, num)

print(max_val)
