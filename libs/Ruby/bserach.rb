# Binary Search Library for Ruby
# All methods assume the array is sorted

# Binary search for element existence
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Boolean] true if exists, false otherwise
def binary_search_exists?(arr, target)
  idx = arr.bsearch_index { |x| x >= target }
  !idx.nil? && arr[idx] == target
end

# Binary search to get element index
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer, nil] Index if found, nil otherwise
def binary_search_index(arr, target)
  idx = arr.bsearch_index { |x| x >= target }
  return nil if idx.nil? || arr[idx] != target
  idx
end

# Find the closest element to the target value
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer] Index of the closest element
def find_closest_index(arr, target)
  return 0 if arr.empty?

  idx = arr.bsearch_index { |x| x >= target }

  # If target is greater than all elements
  return arr.size - 1 if idx.nil?

  # If target is smaller than the first element
  return 0 if idx == 0

  # Compare with the previous element to find the closest
  prev_idx = idx - 1
  (target - arr[prev_idx]).abs < (arr[idx] - target).abs ? prev_idx : idx
end

# Find the closest element value to the target
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Comparable] The closest element value
def find_closest_value(arr, target)
  arr[find_closest_index(arr, target)]
end

# Find the closest smaller or equal element index
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer, nil] Index of the closest element <= target, nil if all elements are greater
def find_closest_le_index(arr, target)
  idx = arr.bsearch_index { |x| x > target }
  return arr.size - 1 if idx.nil?
  return nil if idx == 0
  idx - 1
end

# Find the closest smaller or equal element value
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Comparable, nil] The closest element value <= target, nil if all elements are greater
def find_closest_le_value(arr, target)
  idx = find_closest_le_index(arr, target)
  idx.nil? ? nil : arr[idx]
end

# Find the closest greater or equal element index
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer, nil] Index of the closest element >= target, nil if all elements are smaller
def find_closest_ge_index(arr, target)
  arr.bsearch_index { |x| x >= target }
end

# Find the closest greater or equal element value
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Comparable, nil] The closest element value >= target, nil if all elements are smaller
def find_closest_ge_value(arr, target)
  idx = find_closest_ge_index(arr, target)
  idx.nil? ? nil : arr[idx]
end

# Lower bound: returns the smallest index where arr[i] >= target
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer] Smallest index where arr[i] >= target (arr.size if not found)
def lower_bound(arr, target)
  arr.bsearch_index { |x| x >= target } || arr.size
end

# Upper bound: returns the smallest index where arr[i] > target
# @param arr [Array] Sorted array
# @param target [Comparable] Target value to search
# @return [Integer] Smallest index where arr[i] > target (arr.size if not found)
def upper_bound(arr, target)
  arr.bsearch_index { |x| x > target } || arr.size
end

# Usage examples
if __FILE__ == $0
  arr = [1, 3, 5, 7, 9, 11, 13, 15]

  puts "Array: #{arr}"
  puts

  # Existence check
  puts "binary_search_exists?(arr, 7): #{binary_search_exists?(arr, 7)}"  # => true
  puts "binary_search_exists?(arr, 8): #{binary_search_exists?(arr, 8)}"  # => false
  puts

  # Index retrieval
  puts "binary_search_index(arr, 7): #{binary_search_index(arr, 7)}"  # => 3
  puts "binary_search_index(arr, 8): #{binary_search_index(arr, 8)}"  # => nil
  puts

  # Find closest element
  puts "find_closest_index(arr, 8): #{find_closest_index(arr, 8)}"  # => 3 or 4 (closest to 8)
  puts "find_closest_value(arr, 8): #{find_closest_value(arr, 8)}"  # => 7 or 9
  puts "find_closest_index(arr, 0): #{find_closest_index(arr, 0)}"  # => 0
  puts "find_closest_value(arr, 0): #{find_closest_value(arr, 0)}"  # => 1
  puts "find_closest_index(arr, 100): #{find_closest_index(arr, 100)}"  # => 7
  puts "find_closest_value(arr, 100): #{find_closest_value(arr, 100)}"  # => 15
  puts

  # Find closest smaller or equal element (le = less than or equal)
  puts "find_closest_le_index(arr, 8): #{find_closest_le_index(arr, 8)}"  # => 3 (7 is the closest <= 8)
  puts "find_closest_le_value(arr, 8): #{find_closest_le_value(arr, 8)}"  # => 7
  puts "find_closest_le_index(arr, 7): #{find_closest_le_index(arr, 7)}"  # => 3 (7 itself)
  puts "find_closest_le_value(arr, 7): #{find_closest_le_value(arr, 7)}"  # => 7
  puts "find_closest_le_index(arr, 0): #{find_closest_le_index(arr, 0)}"  # => nil (no element <= 0)
  puts "find_closest_le_value(arr, 0): #{find_closest_le_value(arr, 0)}"  # => nil
  puts

  # Find closest greater or equal element (ge = greater than or equal)
  puts "find_closest_ge_index(arr, 8): #{find_closest_ge_index(arr, 8)}"  # => 4 (9 is the closest >= 8)
  puts "find_closest_ge_value(arr, 8): #{find_closest_ge_value(arr, 8)}"  # => 9
  puts "find_closest_ge_index(arr, 7): #{find_closest_ge_index(arr, 7)}"  # => 3 (7 itself)
  puts "find_closest_ge_value(arr, 7): #{find_closest_ge_value(arr, 7)}"  # => 7
  puts "find_closest_ge_index(arr, 100): #{find_closest_ge_index(arr, 100)}"  # => nil (no element >= 100)
  puts "find_closest_ge_value(arr, 100): #{find_closest_ge_value(arr, 100)}"  # => nil
  puts

  # lower_bound
  puts "lower_bound(arr, 7): #{lower_bound(arr, 7)}"  # => 3 (index of 7)
  puts "lower_bound(arr, 8): #{lower_bound(arr, 8)}"  # => 4 (index of 9)
  puts

  # upper_bound
  puts "upper_bound(arr, 7): #{upper_bound(arr, 7)}"  # => 4 (index of 9)
  puts "upper_bound(arr, 8): #{upper_bound(arr, 8)}"  # => 4 (index of 9)
end
