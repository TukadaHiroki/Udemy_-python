#24, 25はターミナルで実行
#辞書のコピー
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

print("#########")
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)