#20,21はターミナルで実行
#タプルのアンパッキング
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

min, max = 0, 100
print(min, max)

a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
print(a, b, c, d, e, f)

i = 10
j = 20
tmp = i
i = j 
j = tmp
print(i, j)

a = 100
b = 200
a, b = b, a
print(a, b)