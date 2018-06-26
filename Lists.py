ints_and_strings = [1, 2, 3, 'four', 'five', 'spaghet']

sam_height = ['Sam', 67]

heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

ages = [['Aaron', 15], ['Dhruti', 16]]

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
#this will merge the two lists into a 2 dimesional list

print(names_and_dogs_names)
# this will print a zip object and its memory address, not what we want, i.e. "<zip object at 0x7fe18b78b348>"

print(list(names_and_dogs_names))
# this will properly print the lists, i.e.
# [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]

my_empty_list = []
# create an empty list

orders = ['daisies', 'periwinkle']

print(orders)

orders.append('tulips')
# .append adds to end of list
orders.append('roses')

# orders.append('roses', 'petunias')
# this won't work, append takes a single argmumant

print(orders)



my_list = [1, 2, 3]

# my_list + 4
# this won't work, concat ('+') only works with two lists, not other datatypes

new_my_list = my_list + [4]
print(new_my_list)

new_my_list += [5]
print(new_my_list)


orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]



list1 = range(9)
# will create a list of the numbers 0-8
# STUPID PROGRAMMERS STARTING AT '0' lol

print(list1)
#not what we want

print(list(list1))
# that's the stuff!

range1 = range(8)



list1 = range(5, 15, 2)
# counts from 5 to *14*, going by 2's

print(list(list1))
# [5, 7, 9, 11, 13]

list1 = range(5, 15, 3)

list2 = range(0, 40, 5)
#[0, 5, 10, 15 ... 35 ]


first_names = ["Ainsley", "Ben", "Chani", "Depak"]

age = []

age.append(42)

all_ages = age + [32, 41, 29]

name_and_age = zip(first_names, all_ages)

print(list(name_and_age))
#[('Ainsley', 42), ('Ben', 32), ('Chani', 41), ('Depak', 29)]

ids = range(4)

names_and_ages_and_ids = zip(first_names, all_ages, ids)

print(list(names_and_ages_and_ids))
#[('Ainsley', 42, 0), ('Ben', 32, 1), ('Chani', 41, 2), ('Depak', 29, 3)]



last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

subjects.append("computer science")

grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append(("visual arts", 93))

print(list(gradebook))

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
# [('politics', 80), ('latin', 96), ('dance', 97), ('architecture', 65), ('physics', 98),
# ('calculus', 97), ('poetry', 85), ('history', 88), ('computer science', 100),
# ('visual arts', 93)]



#Finding the length of a list
list1 = range(2, 20, 3)

list1_len = len(list1)

print (list1_len)
# prints "6"


employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

# to find the 4th element in the employees list, we would
# write employees[3], since in python
# lists are 0-indexed

index4 = employees[4]
# Gets the 5th element


print(len(employees))
# 7

# print(employees[8])
# IndexError: list index out of range

print(employees[6])
# prints "Robert"



shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))
# 6

last_element = shopping_list[-1]
# -1 is the last element in a list

element5 = shopping_list[5]

print(element5, last_element)
#same thing! "cereal"


# slicing a list
# if we want to get a portion of a list, we do it with the following syntax
# generic_list_name[2:6]. this will return us element 2 through element 5
# (the second argument to a slice will always return that # - 1)


suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:2]

print(beginning)
# prints ['shirt', 'shirt']

beginning = suitcase[0:4]
#grabs first 4 elements: 0,1,2,3

middle = suitcase[2:4]

#we can also omit the first argument to start with [0]:
#suitcase[:2] is the same as "beginning"
#we can omit the second argument to get everything from element X to the end:
#suitcase[4:] would be everything after "middle"

start = suitcase[0:3]
#gives us first three elements

end = suitcase[4:]
#gives us last two elements

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
# .counts sees how many times an item appears in a list

print(jake_votes)
#prints 9

names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()

addresses.sort()
print(addresses)

print(sorted_cities)
#returns none. Super confusing, right?


games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
#now we fixed that nonsense BUT we did
#not change games!

print(games)
print(games_sorted)

#practice:

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)

first = inventory[0]

last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

inventory.sort()


#  ADDITIONAL PRACTICE

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizza = len(toppings)

print("We sell " + str(num_pizza) + " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
#needed to cast it to a list()

pizzas.sort()

sorted(pizzas)

print(pizzas)
# [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'),
# (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]


cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

three_cheapest = pizzas[:3]

print(three_cheapest)
# [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives')]


#Write your function here

def double_index(lst, index):
  if len(lst) > index:
    lst[index] *= 2
    return lst
  else:
    return lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
#prints [3, 8, -20, 12]

# given a list, remove all indidces between
# start and end

def remove_middle(lst, start, end):
  first_half = lst[:start]
  second_half = lst[end + 1:]
  combination = first_half + second_half
  return combination

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
# [4, 23, 42]


# given a list, see if "item" appears more than "n" times
def more_than_n(lst, item, n):
  num_appearances = lst.count(item)
  if num_appearances > n:
    return True
  else:
    return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# True

# given a list, return which item appears more frequently
def more_frequent_item(lst, item1, item2):
  count_item1 = lst.count(item1)
  count_item2 = lst.count(item2)

  if count_item1 >= count_item2:
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
# 3

# given a list, return the middle element
# if the list is even, return average of the two middle elements

def middle_element(lst):
  list_length = len(lst)
  if list_length % 2 == 0:
    middle = int(list_length / 2)
    average_of_middles = (lst[middle - 1] + lst[middle]) / 2
    return average_of_middles
  else:
    return lst[int(list_length/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))
# -7.0

print(middle_element([1, 2, 3]))
# 2


# given a list, take the last two elements, add them together and append that.
# do this a total of three times

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  #this would be better with a for loop
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


# given 2 lists, compare their length
# if lst1 >= lst 2, return last index of lst1
# else return last index of lst2

def larger_list(lst1, lst2):
  len_list1 = len(lst1)
  len_list2 = len(lst2)
  if len_list1 >= len_list2:
    return lst1[-1]
  else:
    return lst2[-1]

#print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
# 5


# given 2 lists, combine them and sort
def combine_sort(lst1, lst2):
  combo_lists = lst1 + lst2
  return sorted(combo_lists)

# print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# [-10, 2, 2, 4, 5, 5, 10, 10]


#Write your function here
def append_size(lst):
  to_append = list(range(1, len(lst)+1))
  lst = lst + to_append
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
