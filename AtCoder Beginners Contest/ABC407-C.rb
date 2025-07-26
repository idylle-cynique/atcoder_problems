# ABC407 - C
# https://atcoder.jp/contests/abc407/tasks/abc407_c

S = gets.chomp

def rotate_number(number, times)
  (number - times) % 10
end

rotate_count = 0

S.reverse.each_char do |c|
  nc = c.to_i
  rotated_nc = rotate_number(nc, rotate_count)

  unless rotated_nc.zero?
    rotate_count += rotated_nc
  end
end

answer = rotate_count + S.length

p answer
