import time

x = 0
y = 0

while True:
    print(x, y)
    x += 1
    y += 1
    time.sleep(1)

    if x and y == 25:
        break
