import numpy as np
import random
import math
import matplotlib.pyplot as plt
import itertools

# Первое задание

x = random.randint(0, 37)
print(x)

# Второе задание (теорема сложения вероятностей)
n = 100
x = []
c = {}

for i in range(0, n):
    a = random.randint(0, 37)
    x.append(a)

for i in x:
    c[i] = c.get(i, 0) + 1

k = list(c.values())

r = sum(k) / n

print(c)

print(r)

# Второе задание (Выборка случайный чисел)


x0 = np.random.rand(n)
x1 = np.random.rand(n)
x2 = np.random.rand(n)
x3 = np.random.rand(n)
x4 = np.random.rand(n)
x5 = np.random.rand(n)
x6 = np.random.rand(n)
x7 = np.random.rand(n)
x8 = np.random.rand(n)
x9 = np.random.rand(n)
f = x0 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
num_bins = 5
n, bins, patches = plt.hist(f, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.savefig('fig.png')

# Третье задание
k1, n1 = 0, 100
a = np.random.randint(0, 2, n1)
b = np.random.randint(0, 2, n1)
c = np.random.randint(0, 2, n1)
d = np.random.randint(0, 2, n1)
x = a + b + c + d
for i in range(0, n1):
    if x[i] == 2:
        k1 = k1 + 1

print (k1, n1, k1/n1)

C1 = math.factorial(n1)/(math.factorial(k1)*math.factorial(n1-k1))
P1 = C1*(1/(2**n1))
print(C1, P1)

# Четвертое задание

for w in itertools.product("34567",repeat=2):
    print(''.join(w))

for w1 in itertools.combinations("34567",4):
    print(''.join(w1))

for w2 in itertools.permutations("34567",3):
    print(''.join(str(x) for x in w2))

# Пятое Задание
n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n


print(a, b)

plt.plot([0, 1], [b, a + b])

xm = sum(x)/n
ym = sum(y)/n
cor = sum((x-xm) * (y-ym)/math.sqrt(sum((x-xm) * (x-xm)) * sum((y-ym) * (y-ym))))
print(cor)




