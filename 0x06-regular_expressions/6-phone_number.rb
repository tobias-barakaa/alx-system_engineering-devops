#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: ./scan_school.rb <string>"
  exit
end

matches = ARGV[0].scan(/^\d{3}-\d{3}-\d{4}( x \d{1,6})?$/)
puts matches.join
