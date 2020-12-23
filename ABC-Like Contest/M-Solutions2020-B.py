# M-Solutions プロコンオープン2020 - B
n,d = [int(x) for x in input().split()]
counts = 0

for i in range(n):
      x,y = [int(x) for x in input().split()]
      if d**2 >= x**2 + y**2:
            counts += 1

print(counts)

# 原点Oと入力された座標(x,y)間の距離とx,yの値の間で三平方の定理が成り立てばいいので、
# math.sqrt()を作らずともd**2 >= x**2 + y**2を条件式にすればいい