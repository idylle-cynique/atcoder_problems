# ABC043 - C

# そのまま要求通りに実装すればよい

s = list(input())
output = []

for key in s:
    if key == "B":
        if len(output) == 0:
            pass
        else:
            output.pop(-1)
    else:
        output.append(key)
    
    #print(output)
print("".join(output))