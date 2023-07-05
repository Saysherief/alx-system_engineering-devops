#!/usr/bin/env ruby

if /hbt{1,4}n/.match?(ARGV[0])
  puts ARGV[0]
else
  puts ""
end
