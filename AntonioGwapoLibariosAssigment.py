print('AnserGwapo')
import matplotlib.pyplot as plt
import math

numeroooo = [x for x in range(1, 10, 1)]

choicerer = {
    1: lambda: [x**2 - 10 for x in numeroooo],
    2: lambda: [x**2 + x - 100 for x in numeroooo],
    3: lambda: [x**10 - x**8 + x**2 - 8 for x in numeroooo],
    4: lambda: [x**4 + x**3 + x**2 + x + 1 for x in numeroooo],
    5: lambda: [(x**2 + x + 10) / (2*x) for x in numeroooo],
    6: lambda: [math.sin(x) / (3*x) for x in numeroooo],
    7: lambda: [x**3 + 2*x**2 - 10*x + 3 for x in numeroooo],
    8: lambda: [math.cos(x) / (5*x) for x in numeroooo],
    9: lambda: [(x**3 / (2*x)) - 10*x for x in numeroooo],
    10: lambda: [(x+2)*(x+3)*(x-4) for x in numeroooo]
}

while True:
    ans = int(input("Pili ka ng number pllslslsl:\n ".center(45, '-')))
    if ans in choicerer:
        result = choicerer[ans]()
        break
    else:
        print("1-10 lng plslslslsl")

plt.plot(numeroooo, color='r')
plt.plot(result, color='b')
plt.xlabel('numeroooo', color='r')
plt.ylabel('Result', color='b')
plt.plot(result, label=f'You chose {ans}', color='g')
plt.legend()
plt.show()