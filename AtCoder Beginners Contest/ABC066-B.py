# ABC066 - B

# 偶文字列とは、要するに文字列を同じ長さで前後二分割したとき同じ値であるもののこと
# したがって、ひとつずつ末尾を削除していき、偶文字列であるような文字列が出来ないか調べ上げればよい

s = input()
s_l = len(s)
ans = ""

for i in range(s_l):
      if (s_l-i)%2 == 0 and i != 0:
            s_f = s[:(s_l-i)//2]       # 文字列の前半分
            s_b = s[(s_l-i)//2:s_l-i]  # 文字列の後半分
            #print(s_l-i,s[:s_l-i]); print(s_f,":",s_b)
            if s_f == s_b: # 前半分と後半分が同じなら、解として値を得てループを終了
                  ans = s_f+s_b
                  break

print(len(ans)) # 解文字列の長さを出力