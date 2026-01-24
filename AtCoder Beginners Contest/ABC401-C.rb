# AtCoder Beginner Contest 401 - C
# https://atcoder.jp/contests/abc401/tasks/abc401_c

MOD = 10 ** 9

def calc(n, k)
  k_bonaccies = Array.new(k) { 1 }
  acm = k_bonaccies.inject([0]) { |acc, e| acc << acc.last + e }

  (k..n).each do |i|
    k_bonaccies << (acm[i] - acm[i - k])
    acm << (acm.last + acm[i] - acm[i - k])%MOD
  end

  k_bonaccies.last%MOD
end

N, K = gets.split.map(&:to_i)

answer = calc(N, K)

p answer