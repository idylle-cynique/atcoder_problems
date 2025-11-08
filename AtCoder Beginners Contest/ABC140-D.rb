# ABC 140 - D
# https://atcoder.jp/contests/abc140/tasks/abc140_d

# Encode an array using run-length encoding
# @param [Array] array Array to encode
# @return [Array<Array>] Array of [element, count] pairs
def run_length_encode(array)
  return [] if array.empty?

  result = []
  current_value = array[0]
  count = 1

  (1...array.size).each do |i|
    if array[i] == current_value
      count += 1
    else
      result << [current_value, count]
      current_value = array[i]
      count = 1
    end
  end

  # Add the last element
  result << [current_value, count]

  result
end

# Encode a string using run-length encoding
# @param [String] str String to encode
# @return [Array<Array>] Array of [character, count] pairs
def run_length_encode_string(str)
  run_length_encode(str.chars)
end

def calc(human_string, human_length, rotate_limit)
  human_rle = run_length_encode_string(human_string)
  max_happiness = human_length - 1 - [human_rle.length - 1 - rotate_limit * 2, 0].max

  max_happiness
end

N, K = gets.split.map(&:to_i)
string = gets.chomp

answer = calc(string, N, K)

p answer