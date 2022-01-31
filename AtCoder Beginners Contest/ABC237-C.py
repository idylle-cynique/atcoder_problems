# ABC237 - C

'''
    挿入する文字が"a"の一種類のみなので、基本的には
        i)  先頭と末尾にある"a"をすべて取り除く
        ii) 残った文字列が回文ならYes, そうでないならNo
    ただし、aaaaaやaabcb、aabcbaのようなこの方針ではYesになってしまう例があるので、
    この例外パターン用の例外処理判定を行う必要がある
'''

String = list(input())

for l in range(len(String)):         # 先頭から何文字目までが"a"かチェック
    if String[l] == "a":
        continue
    else:
        break

for r in range(len(String)-1,-1,-1): # 末尾から何文字目までが"a"かチェック
    if String[r] == "a":
        continue
    else:
        break

#print(l,r); print(String)
l_len = l               # 先頭から連続している"a"の個数
r_len = len(String)-r-1 # 末尾から連続している"a"の個数

#print(l_len,r_len)

if l_len > r_len:      # aabcbaのような場合、"No"
    print("No")
    exit()

String = String[l:r+1] # 残りの文字列を抜き出す

if l == len(String)-1: # aaaaa のような場合、"Yes"
    print("Yes")
    exit()

for idx in range(len(String)):
    if String[idx] == String[len(String)-idx-1]:
        #print(String[idx],String[len(String)-idx-1])
        pass
    else:
        print("No")
        exit()

print("Yes")

