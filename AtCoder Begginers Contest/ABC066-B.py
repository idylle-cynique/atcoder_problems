# ABC066 - B

s = input()
s_l = len(s)
ans = ""

for i in range(s_l):
      if (s_l-i)%2 == 0 and i != 0:
            s_f = s[:(s_l-i)//2]
            s_b = s[(s_l-i)//2:s_l-i]
            #print(s_l-i,s[:s_l-i])
            #print(s_f,":",s_b)
            if s_f == s_b:
                  ans = s_f+s_b
                  break

print(len(ans))