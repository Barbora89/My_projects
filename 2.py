import requests


session = "53616c7465645f5f16b1d4f58d5ce5cbfc485387c152fcabdb07db598b90bdbd5b2056fb98ce8970d2f8c65cfab197ca973f7363fae5cccdb6c15e7fb871f943"

response = requests.get(
    "https://adventofcode.com/2025/day/2/input",
    cookies={"session": session}
)


test_values = response.text.split(',')

invalid = []

for item in test_values:
    value = item.split("-")
    for num in list(map(str,range(int(value[0]), int(value[1]) + 1))):
        quotient, remainder = divmod(len(num), 2)
        first_half, second_half = num[:quotient + remainder], num[quotient + remainder:]
        if first_half in second_half:
            invalid.append(int(num))
print(sum(invalid))


