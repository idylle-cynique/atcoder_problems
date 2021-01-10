n = input()
sum_n = 0
for i in range(len(n)):
      sum_n += int(n[i])

if int(n)%sum_n == 0:
      print("Yes")
else:
      print("No")