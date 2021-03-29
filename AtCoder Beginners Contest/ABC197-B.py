# ABC197 - B

# 要求されたとおりに実装すればよい問題
# 似たようなループを4つ、という構成なのでもっと短いコードに出来る可能性もあるが、
# 本番では確実性を重視して似通ったループ処理を4つ並べるという方法を取った

def view_2dlst(lst):
    for i in lst:
        print(i)
    print()
    return True

h,w,x,y = map(int,input().split())
field = [input() for x in range(h)]

tmp = ["#"*(w+2)]
for i in field:
    tmp.append("#" + i + "#")
tmp.append("#"*(w+2))

#view_2dlst(tmp); print(x,y)

dx = [ 0, 1, 0,-1]
dy = [-1, 0,+1, 0]
ans = 0

if tmp[x][y] == ".":     # 自分のいるマスは「見える」か？
    ans += 1

for i in range(y,w+1):   # 東方向の見えるマスの数を数える
    if tmp[x][i+1] == ".":
        ans += 1
    else:
        break

for i in range(y,-1,-1): # 西方向の見えるマスの数を数える
    #print(tmp[x][i-1],end="")
    if tmp[x][i-1] == ".":
        ans += 1
    else:
        break

for j in range(x,h+1):    # 南方向の見えるマスの数を数える
    if tmp[j+1][y] == ".":
        ans += 1
    else:
        break

for j in range(x,-1,-1):  # 北方向の見えるマスの数を数える
    if tmp[j-1][y] == ".":
        ans += 1
    else:
        break
    
print(ans)