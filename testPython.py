import matplotlib.pyplot as plt

x0 = 0
y0 = 0
xmax = 50

a = input("Entrer a")

b = input("Entrer b")

u = input("Entrer u")

r = a * x0 - b * y0 - u
x = x0
y = y0

while x < xmax:
    x = x + 1
    r = r + a

    if r < 0 or r >= b:
        y = y + 1
        r = r - b

    plt.plot([x], [y])

plt.show()
