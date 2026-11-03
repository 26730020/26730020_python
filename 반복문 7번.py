menu = {1: "ADD", 2: "DELETE", 3: "SEARCH", 4: "PRINT", 5: "EXIT"}

while True:
    num = int(input())
    if num in menu:
        print(menu[num])
        if num == 5:
            break
    else:
        print("ERROR")
