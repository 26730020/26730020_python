password = input()
pattern = input()

five_patterns = pattern * 5

if password in five_patterns:
    print("YES")
else:
    print("NO")
