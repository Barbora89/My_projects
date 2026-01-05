
import requests
from functools import lru_cache


url = "https://adventofcode.com/2025/day/1/input"

@lru_cache(maxsize=10)
def load_values(target_url):
    session = "53616c7465645f5f16b1d4f58d5ce5cbfc485387c152fcabdb07db598b90bdbd5b2056fb98ce8970d2f8c65cfab197ca973f7363fae5cccdb6c15e7fb871f943"
    response = requests.get(target_url,
        cookies={"session": session}
    )
    return response

data = load_values(url).text.strip().splitlines()

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
            if start_position == 0:
                number_of_zeros -= 1
            zeros, new_position = divmod(start_position - rotation, 100)
            number_of_zeros += abs(zeros)
            if start_position != 0 and rotation >= start_position and new_position == 0:
                number_of_zeros += 1
        else:
            zeros, new_position = divmod(start_position + rotation, 100)
            number_of_zeros += zeros
        start_position = new_position
    return number_of_zeros
print(part_2())

























































#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








