#!/usr/bin/env ruby
# A regular expression that must match only CAPITAL LETTERS
puts ARGV[0].scan(/[A-Z]/).join
