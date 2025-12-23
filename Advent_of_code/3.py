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
result = []
for data in  test_data:
    li = list(map(int, str(data)))
    highest = (max(li))
    highest_index = (li.index(highest))

    if highest_index == len(li) - 1:
        second_highest_range = li[:-1]
        second_highest = max(second_highest_range)
        highest_number = str(second_highest) + str(highest)
        result.append(highest_number)

    else:
        second_highest_range = li[highest_index + 1:len(li)]
        second_highest = max(second_highest_range)
        highest_number = str(highest) + str(second_highest)
        result.append(highest_number)
result = list(map(int, result))
print(sum(result))








