# ABC158 - A

# 「A駅とB駅の両方が含まれるときは真・含まれない時(すべてA駅, すべてB駅)は偽をif文で実装すればよい
S = input()

if "A" in S and "B" in S:
    print("Yes")
else:
    print("No")