# CODE FESTIVAL 2016 qual B - B

n, a, b = [int(x) for x in input().split()]
participants = list(input())
passers = []
bs_rank = 1
#print(participants)

for i in range(len(participants)):
      if participants[i] == "a":          # aについて: 合格者数 < A+Bのとき合格
            if len(passers) < a+b:
                  print("Yes")
                  passers.append(i+1)
            else:
                  print("No")
      
      elif participants[i] == "b":        # bについて: 合格者数 < A+B and bの中での順位 <= B
            if len(passers) < a+b and bs_rank <= b:
                  print("Yes")
                  passers.append(i+1)
                  bs_rank += 1
            else:
                  print("No")
                  
      else: # participants[i] == "c"
            print("No")