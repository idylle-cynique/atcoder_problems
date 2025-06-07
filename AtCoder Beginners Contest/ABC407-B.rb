# ABC407 - B 

X, Y = gets.split.map(&:to_i)

all_sum_patterns = Array.new

(1..6).each.with_index do |x, i|
  all_sum_patterns << []
  (1..6).each do |y| 
    all_sum_patterns[i] << x + y
  end
end

all_diff_patterns = Array.new

(1..6).each.with_index do |x, i|
  all_diff_patterns << []
  (1..6).each do |y| 
    all_diff_patterns[i] << (x - y).abs
  end
end

count = 0

all_sum_patterns.zip(all_diff_patterns).each do |sum_pattern, diff_pattern|
  sum_pattern.zip(diff_pattern).each do |sum, diff| 
    count += 1 if sum >= X || diff >= Y
  end
end

answer = (count.to_f / (6 * 6))

puts answer
