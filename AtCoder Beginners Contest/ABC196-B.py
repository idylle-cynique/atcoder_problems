# ABC196 - B

# 入力値を小数値として解釈するのではなく文字列として解釈し、小数点が発生するまでの数字文字列を記録する、という形にすると楽

x = input()
ans = ""

for i in x:
    if i == ".":
        break
    else:
        ans += i

print(ans)