import requests


#numbers = range(11, 22)
#numbers_list = list(map(str,numbers))

session = "53616c7465645f5f16b1d4f58d5ce5cbfc485387c152fcabdb07db598b90bdbd5b2056fb98ce8970d2f8c65cfab197ca973f7363fae5cccdb6c15e7fb871f943"

response = requests.get(
    "https://adventofcode.com/2025/day/2/input",
    cookies={"session": session}
)

"""test_values = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
"1698522-1698528","446443-446449","38593856-38593862"]"""

"""test_values=["565653-565659",
"824824821-824824827","2121212118-2121212124"]"""


test_values = response.text.split(',')

invalid = []

for item in test_values:
    value = item.split("-")
    first_number , second_number = int((value[0])), int((value[1]))
    range_of_numbers = list(map(str,range(int(first_number), int(second_number + 1))))
    #print(range_of_numbers)
    for num in range_of_numbers:
        q, r = divmod(len(num), 2)
        first_half, second_half = num[:q + r], num[q + r:]
        if first_half in second_half:
            invalid.append(int(num))



print(sum(invalid))






























"""for numbers in test_values:
    #numbers = list(map(str,range(numbers)))



invalid = 0
for num in numbers_list:
    res = num in (num + num)[1:-1]
    if res:
        invalid +=1
#print(invalid)"""




# Check if string repeats by slicing and multiplying

