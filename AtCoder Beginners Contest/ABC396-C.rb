# ABC 396 - C
# https://atcoder.jp/contests/abc396/tasks/abc396_c

def calc(black_balls, white_balls)
  total_value = 0
  
  black_balls.sort!.reverse
  white_balls.sort!.reverse
  
  # 両方とも正の値なら取る
  while black_balls.size > 0 && white_balls.size > 0 && black_balls.last > 0 && white_balls.last > 0
    total_value += black_balls.pop
    total_value += white_balls.pop
  end 
  
  # 黒が負でも (白 - 黒) が正なら取る
  while black_balls.size > 0 && white_balls.size > 0 && white_balls.last > 0 && black_balls.last + white_balls.last > 0
    total_value += black_balls.pop
    total_value += white_balls.pop 
  end
  
  # 黒が正なら取る
  while black_balls.size > 0 && black_balls.last > 0
    total_value += black_balls.pop
  end
  
  total_value
end

N, M = gets.split.map(&:to_i)

black_balls = gets.split.map(&:to_i)
white_balls = gets.split.map(&:to_i)

answer = calc(black_balls, white_balls)

p answer
