A, B = input().split()

triple_A = A + A + A

if B in triple_A:
    print(A + B)
else:
    print(B + B)
