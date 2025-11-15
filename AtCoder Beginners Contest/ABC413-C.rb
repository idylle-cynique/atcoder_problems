# ABC 413 - C
# https://atcoder.jp/contests/abc413/tasks/abc413_c

def answer(queries)
  deque = []

  queries.each do |q|
    command, time, element = q

    case command
    when 1
      deque.push([element, time])
    when 2
      total = 0
      rest = time

      while(rest > 0)
        first_element, number_of_elements = deque.shift

        pop_times = [rest, number_of_elements].min
        total += first_element * pop_times
        rest -= pop_times

        if number_of_elements > pop_times
          deque.unshift([first_element, number_of_elements - pop_times])
        end
      end

      p total
    end
  end
end

Q = gets.to_i
queries = Q.times.map { gets.split.map(&:to_i) }

answer(queries)