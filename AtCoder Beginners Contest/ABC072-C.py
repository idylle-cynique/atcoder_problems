n = int(input())
a = sorted([int(x) for x in input().split()])
left,right = 0,0
ans = 0
#print(a)

while(right < n):
      #print(a[left:right],end=":")
      #print(left,right)
      if a[right]-a[left] <=2:
            right += 1
      else:
            left += 1
      
      if right-left > ans:
            ans = right-left

print(ans)