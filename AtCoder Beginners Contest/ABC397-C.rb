# ABC 397 - C
# https://atcoder.jp/contests/abc397/tasks/abc397_c

require 'set'

def update_dict(hash, key, remove = false)
  if remove
    if hash[key] == 1
      hash.delete(key)
    else
      hash[key] -= 1
    end
  else
    if hash.key?(key)
      hash[key] += 1
    else
      hash[key] = 1
    end
  end
  
  hash
end

def calc(arr)
  max_variety = 0
  
  a_counter = Hash.new
  b_counter = arr.tally

  arr.each_with_index do |n,i|
    update_dict(a_counter, n)
    update_dict(b_counter, n, remove = true)

    max_variety = [max_variety, a_counter.size + b_counter.size].max
  end
  
  max_variety
end


N = gets.to_i
array = gets.split.map(&:to_i)

answer = calc(array)

p answer
