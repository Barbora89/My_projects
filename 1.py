
from itertools import cycle, islice

initial_value = 0 # uvodni hodnota
rotated = 5
numbers = list(range(0,100))
numbers_reversed  = list(reversed(range(0,100))) # cisla na ciselniku 0 - 99
cycled_numbers_left = cycle(numbers_reversed)
cycled_numbers_right = cycle(numbers)
sliced_left = list(islice(cycled_numbers_left,numbers_reversed.index(initial_value), numbers_reversed.index(initial_value) + rotated +1))
sliced_right = list(islice(cycled_numbers_right,numbers.index(initial_value), numbers.index(initial_value) + rotated +1 ))
wanted_number_left = sliced_left[-1:]
wanted_number_right = sliced_right[-1:]
print(wanted_number_left)

#print(numbers)
#print(numbers.index(5))
#print(wanted_number_left)









#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








