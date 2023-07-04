#!/usr/bin/env ruby

pattern = /School/

if ARGV.length != 1
  exit
end

string = ARGV[0]

if string =~ pattern
  puts "School"
else
  puts ""
end
