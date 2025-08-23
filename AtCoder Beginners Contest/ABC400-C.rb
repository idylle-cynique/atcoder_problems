# ABC 400 - C
# https://atcoder.jp/contests/abc400/tasks/abc400_c

def isqrt(n)
  return 0 if n == 0
  return 1 if n <= 2 
  return 2 if n == 3
  
  left = 0
  right = n / 2 + 1 
  
  while left <= right
    mid = (left + right) / 2
    square = mid * mid
    
    if square == n
      return mid
    elsif square < n
      result = mid  # midを候補として保存
      left = mid + 1
    else
      right = mid - 1
    end
  end
  
  result
end

def calc(n)
  count = 0
  a = 1
  
  
  while 2 ** a <= n
    max_b = isqrt(n / 2 ** a)
    
    if max_b > 0
      odd_count = (max_b + 1) / 2
      count += odd_count
    end
    
    a += 1
  end
  
  count
end


N = gets.to_i

answer = calc(N)

p answer
