#!/usr/bin/env ruby

if /hb{0,1}tn/.match?(ARGV[0])
  puts ARGV[0]
else
  puts ""
end
