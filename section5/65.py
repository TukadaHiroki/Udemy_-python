# 例外処理
l = [1, 2, 3]
i = 5

try:
    l[0]
except IndexError as exc:
    print("Dont't worry: {}".format(exc))
except NameError as exc:
    print(exc)
except Exception as exc:
    print('other: {}'.format(exc))
else:
    print('done')
finally:
    print('clean up')
