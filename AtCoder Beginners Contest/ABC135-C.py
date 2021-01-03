# ABC135 - C

# そのまま貪欲にモンスターを退治していくだけ？

n = int(input())
monsters = [int(x) for x in input().split()]
slayers = [int(x) for x in input().split()]
monsters_slayed = 0

for i in range(n):
      #print(monsters); print(slayers); print()
      if slayers[i] < monsters[i]: # モンスターの方が多いとき
            monsters_slayed += slayers[i]
            monsters[i] -= slayers[i]
      else: 
            monsters_slayed += monsters[i]
            slayers[i] -= monsters[i]
            monsters[i] = 0
            
            if slayers[i] >= monsters[i+1]:
                  slayers[i] -= monsters[i+1]
                  monsters_slayed += monsters[i+1]
                  monsters[i+1] = 0
            else:
                  monsters[i+1] -= slayers[i]
                  monsters_slayed += slayers[i]
                  slayers[i] = 0
                  
#print(monsters); print(slayers); print()

print(monsters_slayed)