#!/usr/bin/env ruby

if /^\d{10}$/.match?(ARGV[0])
  puts ARGV[0]
else
  puts ""
end
