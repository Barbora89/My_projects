import requests
from functools import lru_cache

url = "https://adventofcode.com/2025/day/2/input"

@lru_cache(maxsize=10)
def load_values(target_url):
    session = "53616c7465645f5f16b1d4f58d5ce5cbfc485387c152fcabdb07db598b90bdbd5b2056fb98ce8970d2f8c65cfab197ca973f7363fae5cccdb6c15e7fb871f943"
    response = requests.get(target_url,
        cookies={"session": session}
    )
    return response

test_values = load_values(url).text.split(',')

def is_repeating(num):
    return num in (num + num)[1:-1]

def part_1():
   invalid = []
   for item in test_values:
     for num in list(map(str,range(int(item.split("-")[0]), int(item.split("-")[1]) + 1))):
         quotient, remainder = divmod(len(num), 2)
         first_half, second_half = num[:quotient + remainder], num[quotient + remainder:]
         if first_half in second_half:
            invalid.append(int(num))
   return sum(invalid)


def part_2():
    invalid = []
    for item in test_values:
        for num in list(map(str, range(int(item.split("-")[0]), int(item.split("-")[1]) + 1))):
            if is_repeating(num):
                invalid.append(int(num))
    return sum(invalid)

print(part_1())
print(part_2())
