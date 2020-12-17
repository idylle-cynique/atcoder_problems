#ABC170 - A
numbers = [int(x) for x in input().split()]
flag = -1
     
for i in range(len(numbers)):
    if numbers[i] == 0:
        flag = i+1
    
print(flag)
