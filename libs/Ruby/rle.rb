# Run Length Encoding (RLE)
# Compress consecutive identical elements into [element, count] format

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

# Usage examples
if __FILE__ == $0
  # Array example
  arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
  encoded = run_length_encode(arr)
  puts "Array encoding:"
  puts "Original: #{arr.inspect}"
  puts "Encoded: #{encoded.inspect}"
  puts "Decoded: #{run_length_decode(encoded).inspect}"
  puts

  # String example
  str = "aaabbbccccdddeee"
  encoded_str = run_length_encode_string(str)
  puts "String encoding:"
  puts "Original: #{str}"
  puts "Encoded: #{encoded_str.inspect}"
  puts "Decoded: #{run_length_decode_to_string(encoded_str)}"
  puts

  # AtCoder style example
  s = "mississippi"
  rle = run_length_encode_string(s)
  puts "AtCoder style:"
  puts "String: #{s}"
  puts "RLE: #{rle.inspect}"
  puts "Character counts:"
  rle.each do |char, count|
    puts "  '#{char}' appears #{count} times"
  end
end
