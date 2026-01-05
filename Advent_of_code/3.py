import requests
from functools import lru_cache

url = "https://adventofcode.com/2025/day/3/input"

@lru_cache(maxsize=10)
def load_values(target_url):
    session = "53616c7465645f5f16b1d4f58d5ce5cbfc485387c152fcabdb07db598b90bdbd5b2056fb98ce8970d2f8c65cfab197ca973f7363fae5cccdb6c15e7fb871f943"
    response = requests.get(target_url,
        cookies={"session": session}
    )
    return response

test_data = load_values(url).text.strip().splitlines()


#test_data = ["987654321111111", "234234234234278", "818181911112111","811111111111119"]

def part_1():
    result = []
    for data in  test_data:
       list_of_numbers = list(map(int, str(data)))
       highest_number = (max(list_of_numbers))

       if list_of_numbers.index(max(list_of_numbers)) == len(list_of_numbers) - 1:
          second_highest = max(list_of_numbers[:-1])
          highest_number = str(second_highest) + str(highest_number)
          result.append(highest_number)

       else:
           second_highest = max(list_of_numbers[list_of_numbers.index(max(list_of_numbers)) + 1:len(list_of_numbers)])
           highest_number = str(highest_number) + str(second_highest)
           result.append(highest_number)
    return sum(list(map(int, result)))

print(part_1())








