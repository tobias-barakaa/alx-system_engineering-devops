#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./scan_school.rb <string>"
  exit
end

matches = ARGV[0].scan(/hbt{0,4}n/)
puts matches.join
