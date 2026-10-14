space = "          "

lines = [
    ("name", "subject"),
    ("minsoo", "math"),
    ("chulsoo", "science")
]

for w1, w2 in lines:
    print(space[:-len(w1)] + w1 + space[:-len(w2)] + w2)
