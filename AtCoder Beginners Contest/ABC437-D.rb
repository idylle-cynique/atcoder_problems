# AtCoder Beginner Contest 437 - D
# https://atcoder.jp/contests/abc437/tasks/abc437_d

# Find the closest smaller or equal element index
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer, nil] Index of the closest element <= target, nil if all elements are greater
def find_closest_le_index(arr, target)
  idx = arr.bsearch_index { |x| x > target }
  return arr.size - 1 if idx.nil?
  return nil if idx == 0
  idx - 1
end

N, M = gets.split.map(&:to_i)
array = gets.split.map(&:to_i).sort
brray = gets.split.map(&:to_i).sort

MOD = 998244353

def calc(arr_a, arr_b)
  total = 0

  acm = arr_a.inject([]) do |arr, e|
    arr.empty? ? arr << e : arr << arr.last + e
  end

  arr_b.each do |n|
    idx = find_closest_le_index(arr_a, n)

    abs_sum = if idx.nil?
                acm.last - n * acm.size
              else
                former_abs_sum = n * (idx + 1) - acm[idx]
                latter_abs_sum = acm.last - acm[idx] - n * (acm.size - idx - 1)

                former_abs_sum + latter_abs_sum
              end

    total =  (total + abs_sum)%MOD
  end

  total
end

answer = calc(array, brray)

p answer