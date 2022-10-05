import re


def find_date(line):
    pattern = "((Mr.|Mrs.|Ms.|Dr.)\s[A-Z]\w*)" #looks for prefix with a capital letter and names
    result = re.findall(pattern,line)

    pattern=r'([A-Z]\w*\s[A-z]\w*)' #looks for two consecutive words starting with capital letters.
    result = result + re.findall(pattern,line)
    pattern=r'([A-Z]\.\s[A-Z]\w*)' #looks for Initial and capitalized last name
    result = result + re.findall(pattern,line)
  
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)

