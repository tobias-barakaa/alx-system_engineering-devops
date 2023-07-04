#!/usr/bin/env ruby

pattern = /School/

if ARGV.length != 1
  puts "Usage: ./0-simply_match_school.rb <string>"
  exit
end

string = ARGV[0]

if string =~ pattern
  puts "School"
else
  puts ""
end
