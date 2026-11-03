menu = {1: "NEW", 2: "OPEN", 3: "SAVE", 4: "QUIT"}

while True:
    num = int(input())
    print(menu.get(num, "AGAIN"))
    if num == 4:
        break
