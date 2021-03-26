n = int(input())
a = [int(x) for x in input().split()]
a_x4 = []
a_x2 = []
a_others = []

# 4の倍数である要素が1つあるか、もしくは2の倍数である要素が2つ並んでいる状態にできれば、条件を満たすことができると言える

for i in a:
        if i%4 == 0: # 4の倍数である要素を集める
                a_x4.append(i)
                continue
        if i%2 == 0: # 4の倍数ではないが2の倍数である要素を集める
                a_x2.append(i)
                continue
        else:        # 4の倍数でも2の倍数でもない要素を集める
                a_others.append(i)

if len(a_x2)%2 == 0: # 4の倍数ではない2の倍数の要素が偶数個あるとき
        if len(a_others)-1 <= len(a_x4): # [1,4,3,8,5] のように、両端に奇数要素、間を縫う形で4の倍数要素を並べる、ということが可能か
                print("Yes")
        else:
                print("No")
else:
        if len(a_others) <= len(a_x4):
                print("Yes")
        else:
                print("No")