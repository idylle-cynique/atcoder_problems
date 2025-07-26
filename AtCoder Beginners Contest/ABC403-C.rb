# ABC 403 - C
# https://atcoder.jp/contests/abc403/tasks/abc403_c

require 'set'

N, M, Q = gets.split.map(&:to_i)

super_users = Set.new([])
user_permissions = Hash.new

def super_user?(super_users, user)
  super_users.include?(user)
end

def permitted_user?(permitted_contests, contest)
  permitted_contests.include?(contest)
end

Q.times do 
  query = gets.split.map(&:to_i)
  
  case query.first
  when 1
    user, contest = query[1..]
    
    if user_permissions.key?(user)
      user_permissions[user].add(contest)
    else
      user_permissions[user] = Set.new([contest])
    end
  when 2
    user = query[-1]
    super_users.add(user)
  when 3
    user, contest = query[1..]
    
    if super_user?(super_users, user)
      puts 'Yes'
    elsif user_permissions.key?(user) && permitted_user?(user_permissions[user], contest)
      puts 'Yes'
    else
      puts 'No'
    end
  end
end
