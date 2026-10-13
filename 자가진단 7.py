h, m = map(int, input().split())

h_str = "0" + str(h - 12 if h > 12 else (12 if h == 0 else h))
m_str = "0" + str(m)

print(h_str[-2:] + " : " + m_str[-2:] + (" PM" if h >= 12 else " AM"))
