# ABC058 - C

# 文字列処理の問題
# 制約上計算量はさして大きくならないが、どのように実装するかで難儀した

import collections

alphs = list("abcdefghijklmnopqrstuvwxyz")

n = int(input())
s = [sorted(input()) for x in range(n)]
check_list = {}

for i in alphs:
      check_list[i] = 0

for i in s[0]:
      check_list[i] += 1

for i in range(1,n):
      temp = collections.Counter(s[i])
      #print(temp); print(check_list)
      for j in alphs:
            #print(j,":",check_list[j],temp[j])
            check_list[j] = min(check_list[j],temp[j])
                # 比較対象とcheck_listのうち、数が少ない方をcheck_listに再代入する

ans = ""

for i,j in check_list.items():
      ans += (i*j)
      
print(ans)