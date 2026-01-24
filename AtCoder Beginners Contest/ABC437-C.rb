# AtCoder Beginner Contest 437 - C
# https://atcoder.jp/contests/abc437/tasks/abc437_c

T = gets.to_i

def greedy_calc(reindeers)
  total_power = reindeers.map(&:last).sum
  total_weight = 0
  sorted_deers = reindeers.sort
  count = 0

  sorted_deers.each do |cost, weight, power|
    break if total_power - power < total_weight + weight

    total_power -= power
    total_weight += weight
    count += 1
  end

  count
end

T.times do
  n = gets.to_i
  cases = n.times.map do
    c = gets.split.map(&:to_i)
    [c.sum, *c]
  end

  t_answer = greedy_calc(cases)

  p t_answer
end