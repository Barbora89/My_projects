
from itertools import cycle, islice

#initial_value = 50 # uvodni hodnota
#given_value = 'L68'
given_value = ["L68","L30" , "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]  # pocet otoceni
#rotated = int(''.join(filter(str.isdigit, given_value))) # pouze cislo
numbers = list(range(0,100))  # cisla na ciselniku 0 - 99
numbers_reversed  = list(reversed(range(0,100))) # ciselnik otaceji se na opacnou stranu
#cycled_numbers_left = cycle(numbers_reversed)
#cycled_numbers_right = cycle(numbers)
#sliced_left = list(islice(cycled_numbers_left,numbers_reversed.index(initial_value), numbers_reversed.index(initial_value) + rotated +1))
#sliced_right = list(islice(cycled_numbers_right,numbers.index(initial_value), numbers.index(initial_value) + rotated +1 ))
#wanted_number_left = sliced_left[-1:]
#anted_number_right = sliced_right[-1:]

def turn_dial(value,sliced_left,sliced_right):
    wanted_number_left = sliced_left[-1:]
    wanted_number_right = sliced_right[-1:]
    if "L" in value:
      return wanted_number_left
    else:
        return wanted_number_right

initial_value = 50

for value in given_value:
     rotated = int(''.join(filter(str.isdigit, value)))
     cycled_numbers_left = cycle(numbers_reversed)
     cycled_numbers_right = cycle(numbers)
     sliced_left = list(islice(cycled_numbers_left, numbers_reversed.index(initial_value), numbers_reversed.index(initial_value) + rotated + 1))
     sliced_right = list( islice(cycled_numbers_right, numbers.index(initial_value), numbers.index(initial_value) + rotated + 1))
     result = turn_dial(value,sliced_left, sliced_right)
     initial_value = result[0]
     print(initial_value)















"""for value in given_value:
    initial_value = 50
    rotated = int(''.join(filter(str.isdigit, value)))
    sliced_left = list(islice(cycled_numbers_left, numbers_reversed.index(initial_value),numbers_reversed.index(initial_value) + rotated + 1))
    sliced_right = list(islice(cycled_numbers_right, numbers.index(initial_value), numbers.index(initial_value) + rotated + 1))"""





























#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








