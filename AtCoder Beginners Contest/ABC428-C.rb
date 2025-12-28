# AtCoder Beginner Contest 428 - C
# https://atcoder.jp/contests/abc428/tasks/abc428_c

Q = gets.to_i
queries = Q.times.map { gets.split }

def good_parentheses?(parentheses, histories)
  histories.empty? || (histories.last.zero? && parentheses.last.zero?)
end

def calc(queries)
  parentheses = []
  state_histories = []

  queries.each do |query|
    case query.first.to_i
    when 1
      new_input = query[1] == '(' ? 1 : -1

      new_parenthesis = parentheses.empty? ? new_input : parentheses.last + new_input
      parentheses << new_parenthesis

      new_state = state_histories.empty? ? parentheses.last : [state_histories.last, parentheses.last].min
      state_histories << new_state
    when 2
      parentheses.pop
      state_histories.pop
    end

    puts good_parentheses?(parentheses, state_histories) ? 'Yes' : 'No'
  end
end

calc(queries)
