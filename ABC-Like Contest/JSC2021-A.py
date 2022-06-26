# JSC2021 - A

# スーパー高橋の牛肉のグラム当たり単価でスーパーすぬけの牛肉を値付けし
# それがスーパーすぬけより安値ならそのまま価格を据え置き、
# 高値ならスーパーすぬけの価格から一円分だけ引けばよい
X,Y,Z = map(int,input().split())

price = Y/X
package = price*Z
#print(price,package)

if int(package) < package:
    print(int(package))
else:
    print(int(package)-1)