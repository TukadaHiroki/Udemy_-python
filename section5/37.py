#値が入っていない判定をするテクニック
#is_ok = True
# False, 0, 0.0, '', [], {}, set()
is_ok = [1, 2, 3]
if is_ok:
    print('OK!')
else:
    print('NO!')