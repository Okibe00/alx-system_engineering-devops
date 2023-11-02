#!/usr/bin/env ruby
# match string with regular expression
puts ARGV[0].scan(/^h.{1}n$/).join
