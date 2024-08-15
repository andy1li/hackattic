# Translated from Python to Ruby by ChatGPT

SAMPLE_INPUT = %w[
  aaaaaiiiixqvsm
  rrdkuuuuyyyrrrrgghc
  xhzzzccccvvsssqppc
  jbiiiulllllvvvvtttttxxxxxs
]

SAMPLE_OUTPUT = %w[
  5a4ixqvsm
  rrdk4u3y4rgghc
  xh3z4cvv3sqppc
  jb3iu5l4v5t5xs
]

def handle_group(char, group)
  size = group.size
  if size == 1
    char
  elsif size == 2
    char * 2
  else
    "#{size}#{char}"
  end
end

def solve(line)
  grouped = line.chars.chunk_while { |i, j| i == j }.to_a
  grouped.map { |group| handle_group(group[0], group) }.join
end

def main
  raise 'Assertion failed' unless SAMPLE_OUTPUT == SAMPLE_INPUT.map { |line| solve(line) }

  ARGF.each_line do |line|
    puts solve(line.chomp)
  end
end

main
