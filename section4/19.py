i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

print('#############')
x = [1, 2, 3, 4, 5]
y= x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

print('#############')
x = 20
y = x
y = 5
print(y)
print(x)
print(id(x))
print(id(y))

print('#############')
x = ['a', 'b']
y = x
y[0] = 'p'
print(y)
print(x)
print(id(x))
print(id(y))