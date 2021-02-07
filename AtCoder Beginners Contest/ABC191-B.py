# ABC191 - B

# 求められている内容自体は至って単純だが、直接受け取った配列にremove()処理などを施すと
# 要素の移動処理に時間がかかりTLEになってしまう
# O(N)で終わらせるために別途解答用配列などを用意するなどの工夫が必要となる

n,x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = ""

for i in a:
      if i != x:
            ans += str(i) + " "

print(ans.strip())