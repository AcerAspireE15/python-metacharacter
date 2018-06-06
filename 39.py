# regular expression

import re

pattern = r"egg"

if re.match(pattern, "baddsfeggbaegggfdesggg"):

    print("'match found")

else:
    print('no match found')


if re.search(pattern, "baddsfeggbaegggfdesggg"):
    print('match found')
else:
    print('no match found')

if re.findall(pattern, "baddsfeggbaegggfdesggg"):
    print('match found')
else:
    print('no match found')

print(re.findall(pattern, "baddsfeggbaegggfdesggg"))


# find and replace

import re

string = "My name is john, Hi I'm john"
pattern = r"john"
newstring = re.sub(pattern, "rob", string)
print(newstring)


# dot metacharacter

import re

pattern = r"gr.y"

if re.match(pattern, "grpy"):
    print('Match found')

# caret and dollar

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print('Match 1')

# character classes

import re

# AA1

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AH8"):
    print('match found')

# star metacharacter

import re

pattern = r"eggs(becon)*"

if re.match(pattern, "eggs"):
    print("match found 1")


# Groups

import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggseggseggsbread"):
    print("match 2")
