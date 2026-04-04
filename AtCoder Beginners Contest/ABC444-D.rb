# AtCoder Beginner Contest 444 - D
# https://atcoder.jp/contests/abc444/tasks/abc444_d

N = gets.to_i
numbers = gets.split.map(&:to_i)

def calc(num_arr)
  digits = Array.new(num_arr.max) { 0 }


  num_arr.each do |n|
    digits[n - 1] += 1
  end

  expanded_arr = expand_arr(digits)
  carried_up_arr = carry_up(expanded_arr)
  carried_up_arr.join
end

# 入力情報を他の桁にも展開する
def expand_arr(num_arr)
  num_arr.reverse.inject([]) do |acc, n|
    acc << (acc.last.to_i + n)
  end
end

def carry_up(num_arr)
  carried_up_arr = []
  carry_up_num = nil

  num_arr.reverse.each do |n|
    if carried_up_arr.empty?
      div, mod = n.divmod(10)
      carried_up_arr << mod
      carry_up_num = div
    else
      carry_up_num, mod = (n + carry_up_num).divmod(10)
      carried_up_arr << mod
    end
  end

  carried_up_arr << carry_up_num if carry_up_num > 0

  carried_up_arr.reverse
end


answer = calc(numbers)

puts answer