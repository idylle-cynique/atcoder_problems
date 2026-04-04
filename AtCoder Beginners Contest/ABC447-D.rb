# AtCoder Beginner Contest 447 - D
# https://atcoder.jp/contests/abc447/tasks/abc447_d

S = gets.chomp.chars

def calc(chars)
  a_cnt, b_cnt, c_cnt = 0, 0, 0

  chars.each do |c|
    case c
    when 'A'
      a_cnt += 1
    when 'B'
      b_cnt = [b_cnt + 1, a_cnt].min
    when 'C'
      c_cnt = [c_cnt + 1, b_cnt].min
    end
  end

  c_cnt
end

answer = calc(S)

p answer