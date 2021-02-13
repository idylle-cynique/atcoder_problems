# ABC086 - C
n = int(input())
s,a,b = 0,0,0

for i in range(n):
      t,x,y = [int(x) for x in input().split()]
      #print(t,x,y,":",s,a,b)
      #print("distance=" + str(abs(x-a)+abs(y-b)),"time=" + str(t-s),end=" "); print("check=" + str(((t-s)-(abs(x-a)+abs(y-b)))))
      if abs(x-a)+abs(y-b) <= (t-s) and ((t-s)-(abs(x-a)+abs(y-b)))%2 == 0:
            s,a,b = t,x,y
            continue
      else:
            print("No")
            exit()
            
print("Yes")