# ABC173 - B
n = int(input())
ac = wa = tle = re = 0
m = [input() for x in range(n)]
for i in range(n):
      if m[i] == "AC":
            ac += 1
      elif m[i] == "WA":
            wa += 1
      elif m[i] == "TLE":
            tle += 1
      else:
            re += 1

print("AC x " + str(ac))
print("WA x " + str(wa))
print("TLE x " + str(tle))
print("RE x " + str(re))