# AtCoder Beginner Contest 382
# https://atcoder.jp/contests/abc382/tasks/abc382_c

N, M = gets.split.map(&:to_i)
gourmets = gets.split.map(&:to_i)
deliciousnesses = gets.split.map(&:to_i)

def build_gourmet_degree_correspondence(gourmets)
  {}.tap do |correspondence|
    gourmets.each_with_index do |gourmet_degree, i|
      correspondence[gourmet_degree] ||= i
    end
  end
end

def build_min_gourmets_array(gourmets)
  min_gourmet_degree = 10**6

  gourmets.filter_map do |gourmet_degree|
    if gourmet_degree < min_gourmet_degree
      min_gourmet_degree = gourmet_degree
    end
  end
end

def find_eater_for_dish(deliciousness, min_gourmets, gourmet_degree_correspondence)
  eater_index = min_gourmets.bsearch_index{ |x| x <= deliciousness }

  return - 1 if eater_index.nil?

  eater = min_gourmets[eater_index]
  gourmet_degree_correspondence[eater] + 1
end

def calc(gourmets, deliciousnesses)
  gourmet_degree_correspondence = build_gourmet_degree_correspondence(gourmets)
  min_gourmets = build_min_gourmets_array(gourmets)
  answer_array = []

  deliciousnesses.each do |deliciousness|
    result = find_eater_for_dish(deliciousness, min_gourmets, gourmet_degree_correspondence)
    answer_array << result
  end

  answer_array
end

answer_array = calc(gourmets, deliciousnesses)

answer_array.each do |answer|
  p answer
end
