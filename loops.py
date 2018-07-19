dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

# using range as the list
promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

# appending A to B
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)

# using "break" will break out of the loop, useful for not having to iterate through every item
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

#we can use "continue" to skip an item in the list if it fails to meet a condition
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

#using while is similar to for, except no predetermined end point
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
	students_in_poetry.append(all_students.pop())

print(students_in_poetry)


#nested for loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for sale in location:
    scoops_sold += sale

print(scoops_sold)


# list comprehension allows us to quickly apply a conditional to a for loop
# basic syntax [ expression for item in list if conditional ]
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
# creates a list, called can_ride_coaster, that contains everyone with height > 161

celsius = [0, 10, 15, 32, -5, 27, 3]

#we can apply an expression as part of list comprehension
fahrenheit = [temp * (9/5) + 32 for temp in celsius]

print(fahrenheit)

# more practice.
single_digits = range(10)

squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit**2)

print(squares)

cubes = [digit**3 for digit in single_digits]

print(cubes)


# prints the last 3 letters of each name concatenated to a string
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first, last):
  first_str = first[len(first) - 3:]
  last_str = last[len(last) - 3: ]
  return first_str + last_str

print(password_generator(first_name, last_name))
# ikouki


# we can do the same thing with negative indexes
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

final_word = company_motto[-4:]


first_name = "Bob"
last_name = "Daily"

# this won't work, strings are immutable
# first_name[0] = "R"

# have to do this :/
fixed_first_name = "R" + first_name[1:]


# don't forget to escape special characters!
password = "theycallme\"crazy\"91"


# writing our own length function :)

def get_length(string):
  count = 0
  for letter in string:
    # python doesn't have this:
    # count++
    count += 1
  return count


  # finding a letter in a word
  def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

  
