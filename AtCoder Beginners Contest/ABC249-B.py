'''ABC249 - B
    問題で要求されている処理をそのまま実装することで正しい解が得られる
'''

String = list(input())

lowerflag,upperflag = False,False # 小文字・大文字の出現の有無を確認するためのフラグ
Alph_set = set(String)

for c in String: # 文字列から一文字ずつ取り出して大文字・小文字のいずれであるかを確認
    if c.isupper(): # 大文字があれば大文字フラグを立てる
        upperflag = True
        continue
    
    if c.islower(): # 小文字があれば小文字フラグを立てる
        lowerflag = True


# 重複を取り除いた文字列中の文字の集合の大きさと元の文字列の大きさが等しければ、重複なしと判定できる
if len(String) == len(Alph_set) and upperflag and lowerflag:
    print("Yes")
else:
    print("No")