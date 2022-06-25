# ACL001 - B

a_min,a_max,b_min,b_max = [int(x) for x in input().split()]
# a <= c <= b <= d もしくは c <= a <= d <= b もしくは
# a <= c <= d <= b もしくは c <= a <= b <= d
if   a_min <= b_min and b_min <= a_max and a_max <= b_max:
      print("Yes")
elif b_min <= a_min and a_min <= b_max and b_max <= a_max:
      print("Yes")
elif a_min <= b_min and b_min <= b_max and b_max <= a_max:
      print("Yes")
elif b_min <= a_min and a_min <= a_max and a_max <= b_max:
      print("Yes")
else:
      print("No")