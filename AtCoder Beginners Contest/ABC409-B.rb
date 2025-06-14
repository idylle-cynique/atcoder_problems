# ABC409 - B
# https://atcoder.jp/contests/abc409/tasks/abc409_b

N = gets.to_i
arr = gets.split.map(&:to_i).sort

answer = 0

(0..N).each do |num|
  cnt = arr.select{ |n| n >= num }.count
  
  answer = num if num <= cnt
end

p answer
