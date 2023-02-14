#Docstringsとは(動画閲覧のみ)
#関数内関数
def outer(a, b):
    
    def plus(c, d):
        return c + d
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)

print('閲覧パーセント =', 55/291*100)