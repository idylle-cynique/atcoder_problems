# AtCoder Beginner Contest 247 - C
# https://atcoder.jp/contests/abc247/tasks/abc247_c

N = gets.to_i

number_strings = (1..N).inject([]) do |arr, n|
  arr << if arr.empty?
           n.to_s
         else
           [arr.last, n, arr.last].join(" ")
         end
end

puts number_strings.last