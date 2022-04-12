import re

test_string = "123abc3455123abc899ABC"
pattern = re.compile(r"123")

# methods to search for matches.

# finditer
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)

# findall
# matches = pattern.findall(test_string)
# for match in matches:
#     print(match)

#match
# match = pattern.match(test_string)
# print(match)

# search
# match = pattern.match(test_string)
# print(match)