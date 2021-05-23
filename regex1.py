import re

# *  - 0 or more of previous character
print(re.findall("ab*c","ac"))
print(re.findall("ab*c","acc"))
print(re.findall("ab*c","abcac"))
print(re.findall("ab*c","abdc"))

# . - any single character
print(re.findall("a.c","abc"))
print(re.findall("a.c","abbc"))
print(re.findall("a.c","ac"))
print(re.findall("a.c","a3c"))

# search - search for particular pattern in a string
match_results = re.search("ab*c","ABBBBBC",re.IGNORECASE)
print(match_results.group())

# sub - substitute replace text in a string that matches a regular expression
string = "Everything is <replaced> if it's in <tags>"
print(string)
string = re.sub("<.*>","ELEPHANTS",string)
print(string)

# sub - non greedy
string = "Everything is <replaced> if it's in <tags>"
string = re.sub("<.*?>","ELEPHANTS",string)
print(string)