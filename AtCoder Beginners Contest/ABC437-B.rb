# AtCoder Beginner Contest 437 - B
# https://atcoder.jp/contests/abc437/tasks/abc437_b

require 'set'

H, W, N = gets.split.map(&:to_i)
grid = H.times.map{ gets.split.map(&:to_i) }
numbers = N.times.map{ gets.to_i }

def calc(grid, numbers)
  max_count = 0

  set_numbers = Set.new(numbers)

  grid.each do |line|
    count = (Set.new(line) & numbers).count

    max_count = [max_count, count].max
  end

  max_count
end

answer = calc(grid, numbers)

p answer