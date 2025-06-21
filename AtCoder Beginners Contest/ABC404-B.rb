# ABC404 - B
# https://atcoder.jp/contests/abc404/tasks/abc404_b

def fetch_field(length)
  f = Array.new
  length.times do 
    f << gets.chomp.split('')
  end
  f 
end

def p_field(field)
  field.each do |l|
    puts l.join
  end
end

def calc_degree_of_match(fa, fb)
  side_size = fa.length
  count = 0
  
  (0...side_size).each do |h|
    (0...side_size).each do |w|
      count += fa[h][w] == fb[h][w] ? 1 : 0 
    end
  end
  
  count
end

def rotate_2d_array(array)
  return [] if array.nil? || array.empty?
  return [[]] if array[0].nil?
  
  array.transpose.map(&:reverse)
end

def calc_answer(field_a, field_b)
  field_size = field_a.length
  rotate = 0
  max_match_degree = 0
  rotated_field = field_a
  min_cost = field_size ** 2 + 3
  
  (0...4).each do |n|
    match_degree = calc_degree_of_match(rotated_field, field_b)
    
    min_cost = [min_cost, (field_size ** 2 - match_degree + n)].min
    
    rotated_field = rotate_2d_array(rotated_field)
  end
  
  min_cost
end

N = gets.to_i
field_a = fetch_field(N)
field_b = fetch_field(N)
answer = calc_answer(field_a, field_b)

p answer
