# ABC187 - C
from collections import Counter

# 問題の意図が上手く掴めないが、ひとまず入出力例の通りに実装

n = int(input())
s = {input() for x in range(n)}
s_data = Counter(s)

#print(s)
#print(s_data)

for i in s:
      if "!"+i in s:
            print(i)
            exit()

print("satisfiable")