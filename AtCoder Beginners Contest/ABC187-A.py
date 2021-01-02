# ABC187- A
a,b = [str(x) for x in input().split()]
s_a = int(a[0]) + int(a[1]) + int(a[2])
s_b = int(b[0]) + int(b[1]) + int(b[2])

if s_a > s_b:
      print(s_a)
else:
      print(s_b)