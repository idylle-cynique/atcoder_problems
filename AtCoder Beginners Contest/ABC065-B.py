# ABC065 - B

n = int(input())
a = [0] + [int(input()) for x in range(n)] # ボタンの番号と添え字の数を一致させるために 予め先頭に[0]を入れておく
button_log = set()
idx = 1

# ボタンの押下記録を集合で管理しておけばよい
# 2のボタンを押す機会が発生した時点までの集合の長さが、必要なボタン押下回数
# 既に押したボタンをもう一度押す機会が発生した場合、ボタンの押下順序が無限ループし、2のボタンを押すことが不可能であると判断できる

while(idx not in button_log):
      #print("extinguished:",idx,"next:",a[idx])
      button_log.add(idx)
      
      if a[idx] == 2:
            print(len(button_log))
            exit()
            
      idx = a[idx]

print(-1)
exit()
