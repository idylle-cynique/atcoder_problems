# AtCoder Beginner Contest 428 - B
# https://atcoder.jp/contests/abc428/tasks/abc428_b

N, K = gets.split.map(&:to_i)
str = gets.chomp.chars

def calc(str, size)
  counter = Hash.new(0)
  max_time = 0

  str.each_cons(size) do |s|
    counter[s.join] += 1

    max_time = [max_time, counter[s.join]].max
  end

  max_appears = counter.select do |key, val|
     val == max_time
  end

  { max_time:, chars: max_appears.keys.sort }
end

answer = calc(str, K)

p answer[:max_time]
puts answer[:chars].join(' ')
