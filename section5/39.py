#while文とcontinue文とbreak文
""" count = 0

while count < 5:
    print(count)
    count += 1 """

count = 0
while True:
    if count >= 5:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1
    
#breakはループから完全に出る
#continueは次の周のループにスキップする