
from itertools import cycle, islice
import requests

session = "53616c7465645f5fa62bf7e14a9ed61a8b7db7ffdd7ebd8ce2243441e2d4bcf916aad443de5f0f29b702e2452b485b94ed881128f2c8877b5b16586e82aa687c"

response = requests.get(
    "https://adventofcode.com/2025/day/1/input",
    cookies={"session": session}
)

given_value = response.text.strip().splitlines()
numbers = list(range(0,100))  # cisla na ciselniku 0 - 99
numbers_reversed  = list(reversed(range(0,100))) # ciselnik otaceji se na opacnou stranu


def turn_dial(value,sliced_left,sliced_right):
    zeros = 0
    if "L" in value:
        for v in sliced_left[1:]:
            if v == 0:
                zeros += 1
        return sliced_left[-1:], zeros
    else:
        for v in sliced_right[1:]:
           if v == 0:
            zeros += 1
        return sliced_right[-1:], zeros

initial_value = 50
number_of_zeros = 0
for value in given_value:
     rotated = int(''.join(filter(str.isdigit, value)))
     cycled_numbers_left = cycle(numbers_reversed)
     cycled_numbers_right = cycle(numbers)
     sliced_left = list(islice(cycled_numbers_left, numbers_reversed.index(initial_value), numbers_reversed.index(initial_value) + rotated + 1))
     sliced_right = list( islice(cycled_numbers_right, numbers.index(initial_value), numbers.index(initial_value) + rotated + 1))
     result, zeros = turn_dial(value,sliced_left, sliced_right)
     number_of_zeros += zeros
     #if result[0] == 0:
         #number_of_zeros += 1
     initial_value = result[0]
print(number_of_zeros)


















"""for value in given_value:
    initial_value = 50
    rotated = int(''.join(filter(str.isdigit, value)))
    sliced_left = list(islice(cycled_numbers_left, numbers_reversed.index(initial_value),numbers_reversed.index(initial_value) + rotated + 1))
    sliced_right = list(islice(cycled_numbers_right, numbers.index(initial_value), numbers.index(initial_value) + rotated + 1))"""





























#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








