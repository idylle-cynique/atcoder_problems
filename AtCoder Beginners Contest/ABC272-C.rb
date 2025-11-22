# ABC 272 - C
# https://atcoder.jp/contests/abc272/tasks/abc272_c

# 偶数になる整数の組み合わせは次のうちのいずれか
# (1) 奇数 + 奇数
# (2) 偶数 + 偶数
# 奇数、偶数がいずれも2つ未満の場合は条件を満たす組み合わせは存在しない (解は -1)
# そうでない場合の解は最も大きい奇数ないし偶数同士の組み合わせ

N = gets.split.map(&:to_i)
arr = gets.split.map(&:to_i)


def calc(numbers)
  odds, evens = numbers.partition {|n| n.odd? }

  return -1 if odds.length < 2 && evens.length < 2

  odd_max_sum = odds.length >= 2 ? odds.sort.last(2).sum : 0
  even_max_sum = evens.length >= 2 ? evens.sort.last(2).sum : 0

  [odd_max_sum, even_max_sum].max
end

answer = calc(arr)

p answer
