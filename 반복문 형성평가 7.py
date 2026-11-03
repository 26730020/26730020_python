menu = {"A": "ADD", "B": "BACK", "C": "COPY", "D": "DELETE", "E": "EXIT"}

while True:
    cmd = input()
    print(menu.get(cmd, "NONE"))
    if cmd == "E":
        break
