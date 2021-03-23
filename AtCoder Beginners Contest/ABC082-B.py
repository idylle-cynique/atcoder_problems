# ABC082 - B

# Pythonの場合文字列の比較もいたって容易なので難しいところはない
# sを昇順に、tを降順にソートして (s<t)==True なら Yes

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