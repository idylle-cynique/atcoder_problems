# ABC 272 - A
# https://atcoder.jp/contests/abc272/tasks/abc272_a

N = gets.to_i
arr = gets.split.map(&:to_i)

def calc(arr)
  arr.sum
end

answer = calc(arr)

p answer