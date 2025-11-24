# ABC271 - C
# https://atcoder.jp/contests/abc271/tasks/abc271_c

require 'set'

N = gets.split.map(&:to_i)
arr = gets.split.map(&:to_i)

comics_map = arr.tally
comics_set = Set.new(arr)
comics = comics_set.to_a.sort
sorted_comic_numbers =

leftover = 0

comics_map.each do |k, v|
  leftover += v - 1 if v > 1
end

target = 0

while true
  current_target = target + 1
  # puts [current_target, leftover, comics_set].join(', ')
  # p comics

  if comics_set.include?(current_target)
    target += 1
    next
  end

  if leftover >= 2
    leftover -= 2
    target += 1
    next
  end

  if leftover > 0 || (comics.last && comics.last > current_target)
    rest = 2 - leftover
    leftover = 0
    flag = rest.times.all? do
      comics.last &&
      comics.last > current_target &&
      comics_set.delete(comics.pop)
    end

    break unless flag

    target += 1
    next
  end

  break
end

p target
