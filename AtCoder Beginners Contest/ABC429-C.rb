# AtCoder Beginner Contest 429 - C
# https://atcoder.jp/contests/abc429/tasks/abc429_c

N = gets.to_i
arr = gets.split.map(&:to_i)

def calc(numbers)
  counter = numbers.tally
  count = 0

  counter.each do |num, cnt|

    if cnt >= 2
      same_values_pattern = cnt * (cnt - 1) / 2
      rest_values_pattern = N - cnt
      count += (same_values_pattern * rest_values_pattern)
    end
  end

  count
end

answer = calc(arr)

p answer