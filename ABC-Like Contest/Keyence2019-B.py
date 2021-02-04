# Keyence Programming Contest 2019 - B

# 気の利いたやり方を探して大分失敗したが、実際にはただ全探索すればよい
# 文字の要素数は制約より最大でも n = 100 なので、Ｏ(N^2)による探索でも十分高速に機能する

s = input()

if "keyence" in s:
      print("YES")
      exit()
      
for l in range(len(s)):
      for r in range(l,len(s)):
            #print(s,s[l:r+1]); print(":",s[:l]+s[r:])
            if s[:l]+s[r:] == "keyence":
                  print("YES")
                  exit()

print("NO")