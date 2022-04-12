import re

# Methods on a match object
# start, end, span, group

test_string = "abc1522abc364uhjkabc"

pattern = re.compile(r"abc")

match = pattern.finditer(test_string)

for i in match:
    print(i.span(), i.start(), i.end(), i.group())