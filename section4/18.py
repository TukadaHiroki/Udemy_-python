#14~17はターミナルで実行
#18リストのメソッド
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))

print('#############')
print(r.count(3))

print('#############')
if 5 in r:
    print('exist')

print('#############')    
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

print('#############')
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)
x = ' '.join(to_split)
print(x)

print(help(list))