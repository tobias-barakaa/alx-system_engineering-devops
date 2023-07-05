#!/usr/bin/env ruby

pattern = /(?<=from:|to:|flags:).+?(?=\])/
log_line = ARGV[0]

matches = log_line.scan(pattern)
result = matches.join(',')

puts result
