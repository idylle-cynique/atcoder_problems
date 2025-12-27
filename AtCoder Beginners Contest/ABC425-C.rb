# AtCoder Beginner Contest 425 - C
# https://atcoder.jp/contests/abc425/tasks/abc425_c

N, Q = gets.split.map(&:to_i)
arr = gets.split.map(&:to_i)
queries = Q.times.map do
  gets.split.map(&:to_i)
end

def generate_acm_sum(arr)
  arr.inject([]) do |acc, e|
    c = acc.empty? ? 0 : acc.last
    acc << c + e
  end
end

def calc(arr, queries)
  pos = 0
  arr_acm = generate_acm_sum(arr)

  queries.each do |query|
    case query.first
    when 1
      c, times = query

      pos = (pos + times) % arr.size
    when 2
      c, l, r = query
      l -= 1
      r -= 1

      lp = (pos + l) % arr.size
      rp = (r + pos) % arr.size
      if rp < lp
        lseg_sum = arr_acm[rp]
        rseg_sum = arr_acm.last - arr_acm[lp - 1]
        seg_sum = lseg_sum + rseg_sum
      else
        seg_sum = lp.zero? ? arr_acm[rp] : arr_acm[rp] - arr_acm[lp - 1]
      end
      p seg_sum
    end
  end
end

calc(arr, queries)