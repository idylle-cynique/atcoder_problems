# ABC410 - C
# https://atcoder.jp/contests/abc410/tasks/abc410_c

N, Q = gets.split.map(&:to_i)

array = Array.new(N) { |i| i+1 }

first_index = 0

Q.times do |q|
  q = gets.split.map(&:to_i)
  
  case q.first
  when 1
    idx, next_num = q.slice(1..)
    idx -= 1
    
    target_idx = (first_index + idx).modulo(N)
    
    array[target_idx] = next_num
  when 2
    idx = q.last - 1
    target_idx = (first_index + idx).modulo(N)
    p array[target_idx]
  when 3
    move = q.last
    
    first_index = (first_index + move).modulo(N)
  end
end
