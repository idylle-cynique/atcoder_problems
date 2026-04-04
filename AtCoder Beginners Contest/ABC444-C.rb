# AtCoder Beginner Contest 444 - C
# https://atcoder.jp/contests/abc444/tasks/abc444_c

require 'set'

N = gets.to_i
A = gets.split.map(&:to_i).sort

def valid_l?(arr, l)
  return false if arr.any? { |n| n > l }

  remainders = arr.reject { |n| n == l }
  return false if remainders.size.odd?
  return true if remainders.empty?

  pair_sum_set = Set.new
  remainders.each.with_index do |n, i|
    pair_sum_set << n + remainders[remainders.size - i - 1]
  end

  pair_sum_set.size == 1 && pair_sum_set.first == l
end

candidates = [A.last, A.first + A.last].uniq
answers = candidates.select { |l| valid_l?(A, l) }

puts answers.join(' ')
