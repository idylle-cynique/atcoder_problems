'''ABC082 - B
    文字列sを辞書順最小の形に、文字列tを辞書順最大の形に並べ直し
    この時に s' < t' が成り立つならYes, そうでなければNo とすればよい
'''

s = input()
t = input()

s = sorted(s)
t = sorted(t,reverse=True)

s = "".join(s)
t = "".join(t)
#print(s); print(t)

if s < t:
    print("Yes")
else:
    print("No")