
import requests

session = "53616c7465645f5fa62bf7e14a9ed61a8b7db7ffdd7ebd8ce2243441e2d4bcf916aad443de5f0f29b702e2452b485b94ed881128f2c8877b5b16586e82aa687c"

response = requests.get(
    "https://adventofcode.com/2025/day/1/input",
    cookies={"session": session}
)

data = response.text.strip().splitlines()


start_position = 50

zeros_during_rotation = 0  #part 2


def part_1():
    number_of_zeros = 0
    start_position = 50
    for value in data:
        rotation = int(''.join(filter(str.isdigit, value)))
        if "L" in value:
            new_position = (start_position + rotation * -1) % 100
        else:
            new_position = (start_position + rotation) % 100
        start_position = new_position
        if start_position == 0:
           number_of_zeros += 1
    return number_of_zeros
print(part_1())

def part_2():
    number_of_zeros = 0
    start_position = 50
    for value in data:
        rotation = int(''.join(filter(str.isdigit, value)))
        if "L" in value:
            old_position = start_position
            if start_position == 0:
                number_of_zeros -= 1
            zeros, position = divmod(start_position - rotation, 100)
            number_of_zeros += abs(zeros)
            if position == 0 and rotation >= old_position and old_position > 0:
                number_of_zeros += 1
        else:
            zeros, position = divmod(start_position + rotation, 100)
            number_of_zeros += zeros
        start_position = position
    return number_of_zeros
print(part_2())

























































#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








