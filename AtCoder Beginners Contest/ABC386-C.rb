# ABC386 - C
# https://atcoder.jp/contests/abc386/tasks/abc386_c

K = gets.to_i
S = gets.chomp
T = gets.chomp

def transformable_by_single_insertion?(source, target)
  return false unless target.length - source.length == 1
  
  si = 0
  ti = 0
  diff_count = 0 
  
  while(si < source.length && ti < target.length && diff_count < 2)
    if  source[si] == target[ti]
      si += 1
      ti += 1
    else
      ti += 1
      diff_count += 1
    end
  end
  
  diff_count < 2
end

def transformable_by_single_deletion?(source, target)
  transformable_by_single_insertion?(target, source)
end 

def transformable_by_single_change?(source, target)
  return false unless source.length == target.length
  
  diff_count = 0
  
  source.each_char.with_index do |c, i|
    next if c == target[i]

    diff_count += 1
    
    break if diff_count > 1 
  end 
  
  diff_count < 2
end

def transformable?(source, target)
  return true if source == target
  
  return true if transformable_by_single_insertion?(source, target)
  
  return true if transformable_by_single_deletion?(source, target)
  
  return true if transformable_by_single_change?(source, target)
  
  false 
end 

def calc(source, target)
  transformable?(source, target) ? 'Yes' : 'No'
end 

answer = calc(S, T)

puts answer
