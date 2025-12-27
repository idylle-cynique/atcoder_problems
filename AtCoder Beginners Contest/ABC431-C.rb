# AtCoder Beginners Contest 431 - C
# https://atcoder.jp/contests/abc431/tasks/abc431_c

N, M, K = gets.split.map(&:to_i)
heads = gets.split.map(&:to_i).sort
bodies = gets.split.map(&:to_i).sort.reverse

def find_closest_le_index(arr, target)
  idx = arr.bsearch_index { |x| x > target }
  return arr.size - 1 if idx.nil?
  return nil if idx == 0
  idx - 1
end

def calc(heads, bodies, target)
  count = 0

  bodies.each do |body|
    idx = find_closest_le_index(heads, body)

    break if idx.nil? || heads.empty?

    count += 1
    heads = heads[0...idx]
  end

  count >= target ? 'Yes' : 'No'
end

answer = calc(heads, bodies, K)

puts answer