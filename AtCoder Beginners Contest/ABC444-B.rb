# AtCoder Beginner Contest 444 - B
# https://atcoder.jp/contests/abc444/tasks/abc444_b

N, K = gets.split.map(&:to_i)

def digit_sum(n)
  n.to_s.chars.map(&:to_i).sum
end

def calc(number, target_number)
  cnt = 0

  (1..number).each do |n|
    cnt += 1 if digit_sum(n) == target_number
  end

  cnt
end

answer = calc(N, K)

p answer