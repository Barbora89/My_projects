

test_data = ["987654321111111", "234234234234278", "818181911112111","811111111111119"]
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








