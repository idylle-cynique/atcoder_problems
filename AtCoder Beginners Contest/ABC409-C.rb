# ABC409 - C
# https://atcoder.jp/contests/abc409/tasks/abc409_c

def calc(n, l, distances)
  return 0 unless l.modulo(3).zero?
  
  coordinates = {0 => 1}
  current_point = 0
  arc_length = l/3

  distances.each do |d|
    current_point = (current_point + d).modulo(l)
    
    if coordinates.key?(current_point)
      coordinates[current_point] += 1
    else
      coordinates[current_point] = 1
    end
  end
  
  answer = 0
  
  coordinates.keys.sort.each do |key|
    break if l/3 < key

    a = coordinates[key] 
    b = coordinates.key?(key + arc_length) ? coordinates[key + arc_length] : 0 
    c = coordinates.key?(key + arc_length * 2) ? coordinates[(key + arc_length * 2).modulo(l)] : 0
    count = a * b * c
    answer += count
  end
  
  answer
end

N, L = gets.split.map(&:to_i)
distances = gets.split.map(&:to_i)

answer = calc(N, L, distances)
p answer
