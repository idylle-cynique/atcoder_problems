# ABC405 - C
# https://atcoder.jp/contests/abc405/tasks/abc405_c

N = gets.to_i
array = gets.split.map(&:to_i)

acmsum = []

array.inject(0) do |res, num| 
  acmsum << res + num 
  res + num 
end

answer = 0

acmsum.each_with_index do |num, idx|
  # p [idx, ":", array[idx], num]
  answer += array[idx] * (acmsum.last - num)
end

p answer
