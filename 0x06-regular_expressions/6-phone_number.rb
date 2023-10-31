#!/usr/bin/env ruby
# match string with regular expression
puts ARGV[0].scan(/\b[0-9]{10}\b/).join
