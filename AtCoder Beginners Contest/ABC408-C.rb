# ABC408 - C

N, M = gets.split.map(&:to_i)
battery_coordinates = Array.new(N + 1) { 0 } 

M.times do
  l,r = gets.split.map(&:to_i)
  battery_coordinates[l - 1] += 1
  battery_coordinates[r] -= 1
end

battery_acm = battery_coordinates.inject([]) { |batteries, x| batteries << (batteries.last.to_i + x) }

answer = battery_acm.first(N).min

p answer
