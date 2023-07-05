#!/usr/bin/env ruby

log_file = ARGV[0]

File.open(log_file, 'r') do |file|
  file.each_line do |line|
    if line.include?('SMS')
      sender = line.match(/\[from:(.*?)\]/)&.captures&.first
      receiver = line.match(/\[to:(.*?)\]/)&.captures&.first
      flags = line.match(/\[flags:(.*?)\]/)&.captures&.first
      
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end
