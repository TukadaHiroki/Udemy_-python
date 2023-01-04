#12.文字列のインデックスとスライス

word = 'python'
#インデックス
print(word[0])
print(word[1])
print(word[-1])
print('############')
#スライス
print(word[0:2])
print(word[:2])
print(word[2:])
print('############')
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)