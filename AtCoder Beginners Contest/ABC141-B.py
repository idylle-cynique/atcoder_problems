# ABC141 - B

# 問題で求められている条件を論理的に整理していくと、
# 奇数番目で(偶数番目に入っているべき)"L"が入っていない、かつ偶数番目で(奇数番目に入っているべき)"R"が入っていないとき"Yes"
# ということになる

s = input()

for i in range(len(s)):
    
    if (i+1)%2 == 1 and s[i] == "L":
        print("No")
        exit()
    
    if (i+1)%2 == 0 and s[i] == "R":
        print("No")
        exit()

print("Yes")