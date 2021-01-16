n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
multa = set()
multb = set()
max_a = 1
max_axb = 0

# 1 <= i <= j <= n を満たすような a_i*b_j

for i in range(n):
    if max_a < a[i]:
        max_a = a[i]
      
    if max_axb < b[i]*max_a:
        max_axb = b[i]*max_a
    #print(b[i],max(multa))
    print(max_axb)
      