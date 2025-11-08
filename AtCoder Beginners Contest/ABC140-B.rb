# ABC 140 - B
# https://atcoder.jp/contests/abc140/tasks/abc140_b

def calc(dishes, gratifications, bonuses)
  pre_dish_idx = nil
  total = 0

  dishes.each do |dish|
    dish_idx = dish - 1
    total += gratifications[dish_idx]

    if pre_dish_idx && pre_dish_idx + 1 == dish_idx
      total += bonuses[pre_dish_idx]
    end
    pre_dish_idx = dish_idx
  end

  total
end

N = gets.to_i
A = gets.split.map(&:to_i)
B = gets.split.map(&:to_i)
C = gets.split.map(&:to_i)

answer = calc(A, B, C)

p answer