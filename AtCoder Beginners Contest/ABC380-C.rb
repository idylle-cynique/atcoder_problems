# ABC 380 - C
# https://atcoder.jp/contests/abc380/tasks/abc380_c

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

# Decode run-length encoded data
# @param [Array<Array>] encoded Array of [element, count] pairs
# @return [Array] Decoded array
def run_length_decode(encoded)
  result = []
  encoded.each do |value, count|
    result.concat([value] * count)
  end
  result
end

# Decode run-length encoded data to string
# @param [Array<Array>] encoded Array of [character, count] pairs
# @return [String] Decoded string
def run_length_decode_to_string(encoded)
  run_length_decode(encoded).join
end

N, K = gets.split.map(&:to_i)
bit_string = gets.chomp

def calc(bit_string, k)
  bit_rle = run_length_encode_string(bit_string)
  true_bit_indices = bit_rle.each_with_index.filter_map do |entry, index|
    bit, count = entry
    index if bit == '1'
  end
  target_index = true_bit_indices[k - 1]
  bit_rle[target_index-1], bit_rle[target_index] = bit_rle[target_index], bit_rle[target_index-1]

  run_length_decode_to_string(bit_rle)
end

answer = calc(bit_string, K)

puts answer