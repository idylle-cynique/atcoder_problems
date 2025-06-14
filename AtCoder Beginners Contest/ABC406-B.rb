# ABC406-B
# https://atcoder.jp/contests/abc406/tasks/abc406_b

N, K = gets.split.map(&:to_i)
numbers = gets.split.map(&:to_i)

def digit(number)
  number.to_s.size
end

def calc(a, b)
  ans = a * b
  if digit(ans) > K 
    1
  else
    ans
  end
end

answer = numbers.inject(1) do |result, num|
  ret = calc(result, num)
  # puts "#{result}, #{num}: #{ret}"
  ret 
end

puts answer
