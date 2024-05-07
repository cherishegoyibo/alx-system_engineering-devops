#!/usr/bin/env ruby
# A regular expression that match a string that starts with h and ends with n, having any single character inbetween
puts ARGV[0].scan(/h.n/).join
