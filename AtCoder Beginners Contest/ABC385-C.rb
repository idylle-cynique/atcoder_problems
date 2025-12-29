# AtCoder Beginner Contest 385 - C
# https://atcoder.jp/contests/abc385/tasks/abc385_c

def calc(arr)
  ans = 1
  arr_size = arr.size

  (0...(arr_size/2)).each do |start|
    max_count = 1

    (start+1...arr_size).each do |step|
      break if start + step >= arr_size

      pre_height = arr[start]
      count = 1

      (start+step).step(by: step, to: arr_size - 1) do |i|
        if pre_height == arr[i]
          count += 1
          max_count = [max_count, count].max
        else
          max_count = [max_count, count].max
          count = 1
          pre_height = arr[i]
        end
      end
    end
    ans = [ans, max_count].max
  end

  ans
end

N = gets.to_i
heights = gets.split.map(&:to_i)

answer = calc(heights)

p answer