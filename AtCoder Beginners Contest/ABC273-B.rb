# ABC 273 - B
# https://atcoder.jp/contests/abc273/tasks/abc273_b

def round_to_digit(n, digit)
  divisor = 10 ** digit
  (n.to_f / divisor).round * divisor
end

def calc(number, digit)
  rounded_number = number
  time = 1
  (1..digit).each do |d|

    rounded_number = round_to_digit(rounded_number, time)

    time += 1
  end

  rounded_number
end

X, K = gets.split.map(&:to_i)

answer = calc(X, K)

p answer