# dictionairies have similar syntax to json
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

# dicts can be empty
my_empty_dictionary = {}

animals_in_zoo = {}

# we add key value pairs similar to JS
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

# print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# adding multiple keys at once is easy enough
user_ids.update({"theLooper":138475, "stringQueen": 85739})

# print(user_ids)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"

# updating a specific key
oscar_winners["Best Picture"] = "Moonlight"


# mapping keys to values
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}


songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] += 5

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)


#accessing elements
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])

print(zodiac_elements["fire"])


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# won't work! Key Error
# print(zodiac_elements["energy"])

zodiac_elements["energy"] = "Not a Zodiac element"



caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha'] = 30
# Adding ways to fail safely!
try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")



user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# safely gets the value from a specified key
# if provided a second argument, that will be # the default return value if it is not found
tc_id = user_ids.get("teraCoder", 100000)

stack_id = user_ids.get("superStackSmash", 100000)

print(stack_id)




# we can use .pop(key, default_value) to delete an item from a dictionary,
# default_value is optional and will be used if no key is found
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(available_items, health_points)

# we can use .keys() to give us a "view object", a list of all the keys in a
# dictionary. THIS IS NOT EDITABLE
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)
print(lessons)

# we can also use list(dictionary) to get just the keys as a lists
usrs = list(user_ids)


# we can use .values to get the values on a dictionary. Not directly editable
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for i in num_exercises.values():
  total_exercises += i

print(total_exercises)

# .items gives us keys and values as a tuple (x, y)
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
  print("Women make up {value} percent of {key}s.".format(value=value, key=key))


# little practice:
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your {key} is the {value} card.".format(key=key, value=value))
