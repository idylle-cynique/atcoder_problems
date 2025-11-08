# ABC 143 - A
# https://atcoder.jp/contests/abc143/tasks/abc143_a

def calc(window_length, curtain_length)
  rest = window_length - curtain_length * 2

  rest > 0 ? rest : 0
end

A, B = gets.split.map(&:to_i)
answer = calc(A, B)

p answer