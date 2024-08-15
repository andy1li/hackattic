# Translated from Python to Ruby by ChatGPT

SAMPLE_INPUT = [
  '#.#.#.###.#.##.#',
  '##.##.......#..#',
  '#..#####..#.#...',
  '###..#....###.##',
  '#..#..#.#....##',
  '#......#.##....',
  '#############.#.'
]

SAMPLE_OUTPUT = %w[
  43949
  55305
  40744
  58427
  18755
  16560
  65530
]

def solve(line)
  x = line.gsub('#', '1').gsub('.', '0')
  x.to_i(2)
end

def main
  raise 'Assertion failed' unless SAMPLE_OUTPUT == SAMPLE_INPUT.map { |line| solve(line).to_s }

  ARGF.each_line do |line|
    puts solve(line.chomp)
  end
end

main
