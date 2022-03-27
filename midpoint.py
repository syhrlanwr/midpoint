import matplotlib.pyplot as plt
import pandas as pd


def midpoint(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    x2 = 2 * x
    y2 = 2 * y
    dict = {
        'Pk': [],
        'X(k+1)': [],
        'Y(k+1)': [],
        '2X(k+1)': [],
        '2Y(k+1)': []
    }
    while x <= y:
        dict['Pk'].append(p)
        yield(xc + x, yc + y)
        yield(xc + y, yc + x)
        yield(xc + x, yc - y)
        yield(xc + y, yc - x)
        yield(xc - x, yc - y)
        yield(xc - y, yc - x)
        yield(xc - x, yc + y)
        yield(xc - y, yc + x)
        x2 = 2 * x + 2
        x += 1
        if p < 0:
            p = p + x2 + 1
        else:
            y2 = 2 * y - 2
            y -= 1
            p = p + x2 - y2 + 1
        dict['X(k+1)'].append(x)
        dict['Y(k+1)'].append(y)
        dict['2X(k+1)'].append(x2)
        dict['2Y(k+1)'].append(y2)
    df = pd.DataFrame(dict)
    print(df)


def main():
    x = int(input("Input x: "))
    y = int(input("Input y: "))
    r = int(input("Input r: "))
    x, y = zip(*midpoint(x, y, r))
    plt.figure(figsize=(5, 5))
    plt.scatter(x, y, marker='s', s=200)
    plt.show()


main()
