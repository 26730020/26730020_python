data = [
    ("item", "count", "price", "rate"),
    ("pen", 20, 100, 50.5),
    ("note", 5, 95, 35.3),
    ("eraser", 110, 97, 14.2)
]

for a, b, c, d in data:
    print(f"{a:>10}{b:>10}{c:>10}{d:>10}")
