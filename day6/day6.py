
input = '''Time:        46     85     75     82
Distance:   208   1412   1257   1410'''

# input = '''Time:      7  15   30
# Distance:  9  40  200'''

def parse_input() -> list[tuple[int]]:
  """
  Returns a list of races
  Each race is a 2-tuple of time,distance
  """
  nums = [[int(x) for x in line.split(':')[1].split(' ') if len(x) > 0] for line in input.split('\n')]
  result = []

  for time, distance in zip(nums[0], nums[1]):
    result.append((time, distance))

  return result

def calc_distance(time_total: int, time_pressed: int) -> int:
  """
  Calculates the distance traveled when the button is pressed
  """
  return (time_total - time_pressed) * time_pressed

def main1():
  inputs = parse_input()

  product = 1

  for total_time, record_distance in inputs:
    num_beaten = 0
    for time_pressed in range(0, total_time + 1):
      distance = calc_distance(total_time, time_pressed)
      if distance > record_distance:
        num_beaten += 1
    product *= num_beaten

  print(product)

def main2():
  inputs = [int(line.split(':')[1].replace(' ', '')) for line in input.split('\n')]

  ways = 0
  for time_pressed in range(0, inputs[0] + 1):
    distance = calc_distance(inputs[0], time_pressed)
    if distance > inputs[1]:
      ways += 1

  print(ways)

if __name__ == '__main__':
  # main1()
  main2()