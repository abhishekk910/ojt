import re

# characters used :- . , ^ , $ ,
# special characters :- \d, \D, \s, \S, \w, \W, \b, \B

dates = '''
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020/12/11
2020-11-11

2020/04/02

2020_04_04
2020_04_04
'''
pattern = re.compile(r'\d{4}[-/]1\d[-/]\d{2}')
matches = pattern.finditer(dates)
for match in matches:
    print(match)



