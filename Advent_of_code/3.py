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


all_results = []

for data in test_data:

    result = []

    list_of_numbers = list(map(int, str(data)))

    highest_number = max(list_of_numbers)

    highest_number_index = list_of_numbers.index(max(list_of_numbers))

    number = 12

    if highest_number_index > len(list_of_numbers) - number:

            highest_number = max(list_of_numbers[:len(list_of_numbers) - number + 1])

            highest_number_index = list_of_numbers.index(highest_number)

    else:
            pass

    result.append(highest_number)

    number = number - 1

    count = 1

    while count < 12:

        rest_of_list = list_of_numbers[highest_number_index + 1:]

        if not rest_of_list:
            break

        next_highest = max(rest_of_list)

        next_highest_index = rest_of_list.index(next_highest)

        if next_highest_index > len(rest_of_list) - number:

             next_highest = max(rest_of_list[:len(rest_of_list) - number + 1])

             next_highest_index = rest_of_list.index(next_highest)

        result.append(next_highest)
        count = count + 1

        highest_number_index = highest_number_index + 1 + next_highest_index

        number = number - 1

    # Convert list to integer number
    result_number = int(''.join(map(str, result)))
    all_results.append(result_number)

total_sum = sum(all_results)
print(f"\nTotal sum: {total_sum}")


    #print(f"Output: {''.join(map(str, result))}")
    #print()

    # new_list = list_of_numbers[highest_number_index + 1:]
        #second_highest = max(new_list)
        #if highest_number_index > len(new_list) -11:
        #highest_number = max(new_list[:len(new_list) -11])
        #print(highest_number)







        #new_list = list_of_numbers[highest_number_index + 1:]
        #print(new_list)


        #while highest_number_index > len(list_of_numbers)  - 12 :

"""highest_number_index = highest_number_index -1
            if highest_number_index == len(list_of_numbers) - 12:
                break
        highest_number = data[highest_number_index]
        result.append(highest_number)
        new_data = data[highest_number_index:]
        print(new_data)
    else:"""





























