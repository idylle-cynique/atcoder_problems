# ABC088 - C

def check_c(box,h,w): # 条件を満たすか検証
    for i in range(3):
        for j in range(3):
            if h[i]+w[j] == box[i][j]:
                pass
            else:
                 return False
     return True
                        
c = [[int(x) for x in input().split()] for y in range(3)]
i,j,k = 0,0,0

for x in range(100+1): # 全探索
    for y in range(100+1):
        for z in range(100+1):
            i = c[0][0]-x
            j = c[1][1]-y
            k = c[2][2]-z
            #print(i,j,k)
                        
            if i>=0 and j>=0 and k>=0:
                h = [i,j,k]
                w = [x,y,z]
                #print(h,"-",w)
                        
                if check_c(c,h,w) == True:
                    print("Yes")#; print("an example of the answers is",h,"-",w)
                    exit()
        
print("No")