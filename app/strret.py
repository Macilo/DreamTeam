# list of unsafe streets
import csv
from pprint import pprint
import re

my_file = open("detailed_hijack_area.txt", "r")
content = my_file.read()
unsafe_list = []
my_file.close()
content_list = content.split(".")
for element in content_list:
    unsafe_list.append(element.strip())

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
    
with open('people.csv', newline='') as file:
    reader = csv.reader(file)
    #res = list(map(tuple, reader))
    for row in reader:
        rr = remove_html_tags(row[0])
        print(list(rr))
#pprint(res)
#print(remove_html_tags('Continue straight to stay on <b>Jan Smuts Ave</b>'))