# AtCoder Beginner Contest 437 - A
# https://atcoder.jp/contests/abc437/tasks/abc437_a

A, B = gets.split.map(&:to_i)

FT_PER_IN = 12

def calc(a, b)
  a * FT_PER_IN + b
end

answer = calc(A, B)

p answer
