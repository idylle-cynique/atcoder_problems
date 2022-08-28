''' ABC232 - D
    問題の処理をそのままBFS(グリッドBFS)を用いて再現・全探索を行い
    その中で解となる値を探索していけばよい
    ここでは自作のグリッドBFS関数を問題の処理内容に沿うように処理内容を
    修正のうえ用い、そこから解となる値を戻り値として返させている
'''

from collections import deque

H,W = map(int,input().split())
Field = []
DistMap = [[0] * (W+2) for _ in range(H+2)]
answer = 0

for i in range(H+2):    # グリッド文字列を受取、int値に変換してマップ情報とする
    if i == 0 or i == H+1:
        Field.append(list([-1] * (W+2)))
        continue
    
    tmp = list(input())
    tmp_row = [-1]
    for j in range(len(tmp)):
        if tmp[j] == "#":
            tmp_row.append(-1)
        else:
            tmp_row.append(0)
    tmp_row.append(-1)
    Field.append(tmp_row)
    
def view_distmap(distmap):
    for row in distmap:
        print(row)
    print()
    return True
sx,sy = 1,1

def Grid_BFS(field,x,y):
    ny,nx = y,x
    dx = [ 0,+1]
    dy = [+1, 0]
    DistMap[ny][nx] = 1
    queue = deque()
    queue.append([ny,nx])
    answer = DistMap[ny][nx]
    field[ny][nx] = 1

    while(queue):
        #print(queue)
        ny,nx = queue.popleft()
        for k in range(len(dx)):
            if field[ny+dy[k]][nx+dx[k]] == 0:
                queue.append([ny+dy[k],nx+dx[k]])
                DistMap[ny+dy[k]][nx+dx[k]] = DistMap[ny][nx] + 1
                field[ny+dy[k]][nx+dx[k]] = 1
                answer = max(answer,DistMap[ny+dy[k]][nx+dx[k]])
    
    #view_distmap(DistMap)
    return answer

#view_distmap(Field)
Answer = Grid_BFS(Field,sx,sy)

print(Answer)