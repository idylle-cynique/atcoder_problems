# ABC122 - C

n,q = [int(x) for x in input().split()]
s = input()
accm = [0]
cnt = 0

for i in range(1,n):
      if s[i-1:i+1] == "AC":
            cnt += 1
            accm.append(cnt)
      else:
            accm.append(cnt)

#print(len(accm),accm); print(len(s)   ,(s))

for i in range(q):
      l,r = [int(x) for x in input().split()]
      l,r = l-1,r-1
      #print(s[l:r]);
      print(accm[r]-accm[l])