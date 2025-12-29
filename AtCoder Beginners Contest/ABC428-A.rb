def calc(speed, move_sec, pause_sec, hold_sec)
  div, rest_time = hold_sec.divmod(move_sec + pause_sec)
  time = div * move_sec * speed
  time += (rest_time > move_sec ? move_sec * speed : rest_time * speed)
end

S, A, B, X = gets.split.map(&:to_i)

answer = calc(S, A, B, X)

p answer