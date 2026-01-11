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


"""def part_1():
    result = []
    for data in  test_data:
       list_of_numbers = list(map(int, str(data)))
       highest_number = (max(list_of_numbers))

       if list_of_numbers.index(max(list_of_numbers)) == len(list_of_numbers) - 1:
          highest_number = str(max(list_of_numbers[:-1])) + str(max(list_of_numbers))
          result.append(highest_number)

       else:
           second_highest = max(list_of_numbers[list_of_numbers.index(max(list_of_numbers)) + 1:len(list_of_numbers)])
           highest_number = str(highest_number) + str(second_highest)
           result.append(highest_number)
    return sum(list(map(int, result)))"""

#print(part_1())


result =[]
#count = 0
#count_of_numbers = 12

for data in test_data:
    count = 0
    count_of_numbers = 12
    highest_numbers = []
    list_of_numbers = list(map(int, str(data)))
    highest_number = max(list_of_numbers[:len(list_of_numbers) - count_of_numbers +1])
    highest_numbers.append(highest_number)
    count += 1
    count_of_numbers -= 1
    current_position = list_of_numbers.index(highest_number)
    while count < 12:
      updated_list = list_of_numbers[current_position+1  : len(list_of_numbers)+1 - count_of_numbers]
      if not updated_list:  # Safety check
          break
      #print(updated_list)
      highest_number = max(updated_list)
      highest_numbers.append(highest_number)
      current_position = current_position + 1 + updated_list.index(highest_number)
      count += 1
      count_of_numbers -= 1
    #result_number = int(''.join(map(str, highest_numbers)))
    result.append(int(''.join(map(str, highest_numbers))))
print(sum(result))









"""while count < 13:
        for data in test_data:
            list_of_numbers = list(map(int, str(data)))
            highest_number = max(list_of_numbers[:len(list_of_numbers) - count_of_numbers])
            result.append(highest_number)
            count += 1
            count_of_numbers -= 1
            updated_list = list_of_numbers[list_of_numbers.index(highest_number): len(list_of_numbers) - count_of_numbers]
            highest_number = max(updated_list)
            result.append(highest_number)
print(result)"""












"""all_results = []

for data in test_data:

    result = []

    list_of_numbers = list(map(int, str(data)))

    highest_number = max(list_of_numbers)

    highest_number_index = list_of_numbers.index(max(list_of_numbers))

    count_of_numbers = 12


    if highest_number_index > len(list_of_numbers) - count_of_numbers:

            highest_number = max(list_of_numbers[:len(list_of_numbers) - count_of_numbers + 1])

            highest_number_index = list_of_numbers.index(highest_number)

    else:
        pass

    result.append(highest_number)

    count_of_numbers = count_of_numbers - 1

    count = 1

    while count < 12:

        rest_of_list = list_of_numbers[highest_number_index + 1:]

        next_highest = max(rest_of_list)

        next_highest_index = rest_of_list.index(next_highest)

        if next_highest_index > len(rest_of_list) - count_of_numbers:

             next_highest = max(rest_of_list[:len(rest_of_list) - count_of_numbers + 1])

             next_highest_index = rest_of_list.index(next_highest)

        result.append(next_highest)
        count = count + 1

        highest_number_index = highest_number_index + 1 + next_highest_index

        count_of_numbers = count_of_numbers - 1

    # Convert list to integer number
    result_number = int(''.join(map(str, result)))
    all_results.append(result_number)

print(sum(all_results))"""




































