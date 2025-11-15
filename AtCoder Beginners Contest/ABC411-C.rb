# ABC 411 - C
# https://atcoder.jp/contests/abc411/tasks/abc411_c

def count_number_of_segments(le, ce, re)
  case [le, ce, re]
  when [false, true, false]
    1
  when [true, false, true]
    1
  when [true, true, true]
    -1
  when [false, false, false]
    -1
  when [nil, true, false]
    1
  when [nil, false, false]
    -1
  when [false, true, nil]
    1
  when [false, false, nil]
    -1
  when [nil, true, nil]
    1
  when [nil, false, nil]
    -1
  else
    0
  end
end

def answer(array_length, queries)
  array = Array.new(array_length) { false }
  seg = 0

  queries.each do |n|
    idx = n - 1
    lidx = idx - 1
    ridx = idx + 1

    array[idx] = !array[idx]

    current_door = array[idx]
    left_door = lidx >= 0 ? array[lidx] : nil
    right_door = ridx < array.length ? array[ridx] : nil

    seg += count_number_of_segments(left_door, current_door, right_door)

    p seg
  end
end

N, Q = gets.split.map(&:to_i)
queries = gets.split.map(&:to_i)

answer(N, queries)
