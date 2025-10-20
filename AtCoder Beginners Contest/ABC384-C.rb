# ABC384 - C
# https://atcoder.jp/contests/abc384/tasks/abc384_c

points = gets.split.map(&:to_i)
problems = %i(A B C D E)

def calc(problems, points)
  point_allocation = {}
  problems.zip(points).each { |alph, point| point_allocation[alph] = point } 
  contestant_scores = {}

  (1...(1 << point_allocation.size)).each do |bit|
    answer_problems = problems.select.with_index{ |_, i| bit[i] == 1 }
    
    score = answer_problems.map do |problem|
      point_allocation[problem]
    end.sum
    
    if contestant_scores.key?(score)
      contestant_scores[score] << answer_problems.join
    else
      contestant_scores[score] = [answer_problems.join]
    end
  end
  
  ranking = []
  
  contestant_scores.keys.sort.reverse.each do |score|
    contestant_scores[score].sort.each do |contestant| 
      ranking << contestant
    end
  end
  
  ranking 
end

answer_data = calc(problems, points)

answer_data.each do |answer|
  puts answer
end
