# string method learning

my_name = "Donovan"

# strings are lists!
first_initial = my_name[0]

# we can slice similarly
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

first_name = "Julie"
last_name = "Blevins"

# we can slice and concatenate
def account_generator(first, last):
  return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)


# we can use "in" to figure out if a character or string exists in a second strings
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if letter in string_two and letter not in common:
      common.append(letter)
  return common

# more PRACTICE
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password



poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_text = "HSAHFOHFSAasofhaosfhOHOOFHSOH"

# note that string methods do not change the original string! We need to
# save it to it's own lil thing

# title uppercases each word
poem_title_fixed = poem_title.title()
# upper is to upper case (everything)
poem_author_fixed = poem_author.upper()
#  lower shifts everything to lowercase
poem_text.lower()


# .split splits a string based on a character. with no arguments, splits spaces
line_one = "The sky has given over"

line_one_words = line_one.split()

line_one_stupid = line_one.split("h")

print(line_one_words, line_one_stupid)

# When you split a string on a character that it also ends with,
# you'll end up with an empty string at the end of the list.


# Here we want only the last names of author. Have to do a little dancing
# to make it work

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

# first we split each name out
author_names = authors.split(", ")

# setup an empty list, then iterate through the names
author_last_names = []
for name in author_names:
# now we split the names on the space, and select the last one. This gets around
# the "william carlos williams" issue.
  temp_name = name.split()
  author_last_names.append(temp_name[-1])

print(author_last_names)


spring_storm_text = \
"""The sky has given over
its bitterness.
Out of the dark change
all day long
rain falls and falls
as if it would never end.
Still the snow keeps
its hold on the ground.
But water, water
from a thousand runnels!
It collects swiftly,
dappled with black
cuts a way for itself
through green ice in the gutters.
Drop after drop it falls
from the withered grass-stems
of the overhanging embankment."""

# we can split on the new line character, or even tabs ("\t")
spring_storm_lines = spring_storm_text.split("\n")

# we can join a list into a string in the following way:
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

# note that whatever we put before the join will be the way they join together,
# so ' ' will produce the string with a space between list elements
reapers_line_one = ' '.join(reapers_line_one_words)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

# joining based on new lines
winter_trees_full = "\n".join(winter_trees_lines)



# we can use .strip to strip out leading and trailing spaces
# or we can provide it an argument ('!') to strip leading and trailing characters
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for item in love_maybe_lines:
  love_maybe_lines_stripped.append(item.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)


# we can use replace on a string to replace the first argument with the second argument
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
# so we're replacing "Tomer" with "Toomer"
toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")

# we can find a sequence in a string by using .find(ARG) this will return the
# first index where that string begins to appear, as an int
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")


# .format() takes variables as an argument and includes them in the string that
# it is run on. You include {} marks as placeholders for where those variables will be imported.
def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)


# we can also make these explicit through Keywords
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)







# application and practice: make a little program that, given an ugly list,
# cleans it up and prints a string

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")

#print(highlighted_poems_list)

highlighted_poems_stripped = []

for item in highlighted_poems_list:
  highlighted_poems_stripped.append(item.strip())

#print(highlighted_poems_stripped)

highlighted_poems_details = []

for item in highlighted_poems_stripped:
  highlighted_poems_details.append(item.split(":"))

#print(highlighted_poems_details)
titles = []
poets = []
dates = []

for work in highlighted_poems_details:
  titles.append(work[0])
  poets.append(work[1])
  dates.append(work[2])

def format_the_poem(title, poet, date):
  print("The poem {title} was published by {poet} in {date}".format(title=title, poet = poet, date = date))
  return

for item in range(0,len(titles)-1):
  format_the_poem(titles[item], poets[item], dates[item])
