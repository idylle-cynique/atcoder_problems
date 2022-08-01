''' ABC262 - A
    4の余り値を元に分岐するだけでよい
    ここでは公式解説と異なり余り値が2未満(0,1)のときをまとめて3つの分岐で
    処理を行っているが、特に処理内容に違いはない
'''

YEAR = int(input())
mod = (YEAR%4)

if mod == 2:
    answer = YEAR
elif mod < 2:
    answer = YEAR - mod + 2
else:
    answer = YEAR - mod + 6

print(answer)