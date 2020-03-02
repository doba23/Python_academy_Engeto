import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y = 2 * x + 5
    return y
x = np.arange(0, 10)
y = func(x)

print(y)
plt.title('Nadpis')
plt.xlabel('a label a')

plt.plot (x, y)
plt.show()