n = [int(x) for x in input().split()]
ans = 0

while(n[0] != n[1] or n[1] != n[2]):
      #print(n)
      
      max_idx = n.index(max(n))     # 最大値を取る要素の添え字を取得
      min_idx = n.index(min(n))     # 最小値を取る要素の添え字を取得
      if   max_idx+min_idx == 3:    # 中央値を取る要素の添え字を取得
            mid_idx = 0
      elif max_idx+min_idx == 2:
            mid_idx = 1
      else:
            mid_idx = 2
            
      #print(":",max_idx,mid_idx,min_idx)
      
      if n[max_idx] > n[mid_idx]:   # 最大値よりも小さい値が存在する場合はそれ以外の値を1ずつ増やす
            n[min_idx] += 1
            n[mid_idx] += 1
      else:                         # 最大値と同じ値が存在する場合は最小値を2増やす
            n[min_idx] += 2
            
      ans += 1

print(ans)#; print(n)