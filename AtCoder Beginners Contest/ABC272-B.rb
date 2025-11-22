# ABC 272 - B
# https://atcoder.jp/contests/abc272/tasks/abc272_b

require 'set'

N, M = gets.split.map(&:to_i)

members = {}
N.times{ |n| members[n+1] = Set.new((1..N).to_a) }
parties = M.times.map do
  k, *arr = gets.split.map(&:to_i)
  arr
end

def calc(n, m, members, parties)
  parties.each do |party|
    party.each do |key|
      party.each do |val|
        members[key].delete(val)
      end
    end
  end

  members.values.all?{ |vals| vals.empty? } ? 'Yes' : 'No'
end

answer = calc(N, M, members, parties)

puts answer
