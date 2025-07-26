# ABC398 - C
# https://atcoder.jp/contests/abc398/tasks/abc398_c

require 'set'

N = gets.to_i
array = gets.split.map(&:to_i)

def calc(array)
  corresponding_hash = Hash.new
  
  duplicate_number = Set.new([])
  unique_member = Set.new([])
  
  array.each.with_index do |n, i|
    if corresponding_hash.key?(n)
      corresponding_hash[n].add(i)
    else
      corresponding_hash[n] = Set.new([i])
    end
  end
  
  max_number = -1
  
  corresponding_hash.each do |k, vs|
    next if vs.size > 1
    
    max_number = [max_number, k].max
  end
  
  max_number < 0 ? -1 : corresponding_hash[max_number].first + 1
end

answer = calc(array)

p answer
