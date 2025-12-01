
from itertools import cycle, islice

initial_value = 52 # uvodni hodnota
rotated = 48
numbers  = list(range(0,100)) # cisla na ciselniku 0 - 99
cycled_numbers = cycle(numbers)
sliced = list(islice(cycled_numbers,numbers.index(initial_value), numbers.index(initial_value) + rotated + 1 ))
wanted_number = sliced[-1:]
#print(numbers)
#print(numbers.index(5))
print(wanted_number)









#numbers_cycle = start_from
#result = numbers_cycle[5]
#result = list(num for num in filterfalse(lambda x: x < 4, numbers_cycle))
#esult = list(filterfalse(lambda x: x==20, numbers_cycle))
#print(result)








