# ABC158 - C

a,b = [int(x) for x in input().split()]

      # 制約が 1 <= a <= b <= 10 ということは、
      # 力業的に1から正整数値を全探索していっても正答を得るまでに必要なループ回数は最大でも100/0.08 = 1250程度
      
for i in range(1,1250+1,+1):
      x = int(i*0.08)
      y = int(i*0.10)
      
      #print(n,":",int(n*0.08),int(n*0.1))
      
      if x == a and y == b:
            print(i)
            exit()

print(-1)