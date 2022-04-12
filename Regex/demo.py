# import re
# import paramiko
#
# test_string = 'python-engineer.com'
# pattern = re.compile(r'\.')
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)

import re

test_string = "abc.ac.dea"
pattern = re.compile(r"\.")

match = pattern.findall(test_string)
print(match)
