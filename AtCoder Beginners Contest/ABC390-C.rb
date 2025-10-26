# ABC390 - C
# https://atcoder.jp/contests/abc390/tasks/abc390_c

H, W = gets.split.map(&:to_i)

field = (0...H).map{ gets.chomp.chars }

def p_field(arr2d)
  arr2d.each { |line| puts line.join }
end

def fetch_area_coordinates(arr2d)
  top, left, bottom, right = [nil, nil, nil, nil]
  arr2d.each.with_index do |arr, y|
    arr.each.with_index do |square, x|
      next if square != '#'

      top = y if top.nil?

      left = x if left.nil?

      left = x if x < left

      right = x if right.nil?

      right = x if x > right

      bottom = y if bottom.nil?

      bottom = y if y > bottom
    end
  end

  [top, left, bottom, right]
end

def white_square_include?(arr2d, top, left, bottom, right)
  arr2d[top..bottom].each do |arr|
    arr[left..right].each do |square|
      return true if square == '.'
    end
  end
  return false
end

def calc(arr2d)
  t, l, b, r = fetch_area_coordinates(arr2d)

  white_square_include?(arr2d, t, l, b, r) ? 'No': 'Yes'
end

answer = calc(field)

puts answer