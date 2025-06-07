# ABC408 - B 

N = gets.to_i
array = gets.split.map(&:to_i)

answer = array.uniq.sort

puts answer.size
puts answer.join(" ")
