# AGC022 - A

S = list(input())
S_set = set(S)

alphs = "abcdefghijklmnopqrstuvwxyz"
alphs_set = set(alphs)
alphs_dict = {}

for n in range(len(alphs)):
    alphs_dict[alphs[n]] = n

if len(S) != len(S_set) or S == list("zyxwvutsrqponmlkjihgfedcba"):
    print(-1)
    exit()
else:
    pass

if len(S) == 26:
    poped_chars = []
    while(True):
        #print("".join(S));    print("".join(poped_chars))
        c = S.pop()
        if c == "z" or alphs[alphs_dict[c]+1] in S:
            pass
        else:
            S.append(alphs[alphs_dict[c]+1])
            break
        poped_chars.append(c)
else:
    #print("pattern 2")
    for c in alphs:
        if c not in S_set:
            S.append(c)
            break
    
answer = "".join(S)
print(answer)