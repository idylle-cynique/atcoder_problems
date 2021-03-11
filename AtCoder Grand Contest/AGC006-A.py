# AGC006 - A

# 文字列sをある区間で2つに分けたとき、後ろ(右側)の区間が文字列tに含まれていればいい
# 0 (空文字列と文字列s)から始めていけば考えられる最大の長さが自動的に一番最初に現れる

n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i:] in t:
        ans = s[:i] + t
        print(len(ans))
        exit()

print(n*2)