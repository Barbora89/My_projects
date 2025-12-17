
from itertools import cycle, islice
import requests

session = "53616c7465645f5fa62bf7e14a9ed61a8b7db7ffdd7ebd8ce2243441e2d4bcf916aad443de5f0f29b702e2452b485b94ed881128f2c8877b5b16586e82aa687c"

response = requests.get(
    "https://adventofcode.com/2025/day/1/input",
    cookies={"session": session}
)

rotations = response.text.strip().splitlines()
#rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


initial_value = 50
number_of_zeros = 0
zeros_during_rotation = 0  #part 2

for value in rotations:
    if "L" in value:
        rotation = int(''.join(filter(str.isdigit, value)))
        old_initial_value = initial_value
        if initial_value == 0:
            zeros_during_rotation -= 1
        number_of_rotations, new_value = divmod(initial_value - rotation ,   100)
        zeros_during_rotation += abs(number_of_rotations)
        if new_value == 0 and rotation >= old_initial_value and old_initial_value > 0:
            zeros_during_rotation += 1
        initial_value = new_value

    else:
        rotation = int(''.join(filter(str.isdigit, value)))
        number_of_rotations, new_value = divmod(initial_value + rotation ,   100)
        zeros_during_rotation += number_of_rotations
        initial_value = new_value

    if initial_value == 0:
        number_of_zeros += 1
print(number_of_zeros)
print(zeros_during_rotation)






































#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








