# ABC190 - B

n,s,d = [int(x) for x in input().split()]

for i in range(n):
      x,y = [int(x) for x in input().split()]
      
      if x < s and y > d:
            print("Yes")
            exit()
            
print("No")