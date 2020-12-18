#ABC170 - B

atama, asi = [int(x) for x in input().split()]
if asi%2 == 0 and asi >= atama*2 and asi <= atama*4:
    print("Yes")
else:
    print("No")
     
    # 足の総数は常に偶数
    # 鶴が多いほど、少ない足で頭数を揃えられる
    # 亀が多いほど、頭数に対して足の数が必要