# 三井住友銀行プログラミングコンテスト2019 - B

price = int(input())

prime_cost = int(price / 1.08)

if (prime_cost * 1.08)//1 == price:
      print(prime_cost)
elif ((prime_cost + 1) * 1.08)//1 == price:
      print(prime_cost + 1)
else:
      print(":(")