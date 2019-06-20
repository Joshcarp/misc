# Generates pseudo swagger from xml file, doesn't need valid xml as it uses regex
# run by running commans 'python swaggerFromXML.py FILENAME'
#
#
import re
import sys
keys = ["name", "uri"]
enclosing = "tag"
file = sys.argv[1]
file = open(file)
file = file.read().strip()
# (?s)(?:<{tag}.*?)(?:{key}=\"(.*?)\")(?:.*?)(?:<\/{tag}>) #full regex
regex = f"(?s)(?:<{tag}.*?)(.*?)(?:<\/{tag}>)"
lines = re.findall(regex, file)
matches = []

for line in lines:
    tempdict = {}
    for key in keys:
        regex = f"(?s)(?:{key}=\"(.*?)\")(?:.*?)"
        tempdict[key] = re.findall(regex, line)[0]
    matches.append(tempdict)


for dict in matches:
    temp2 = dict["name"]
    temp1 = dict["uri"]
    print(f"paths:\n    {temp1}:\n        post:\n            summary:{temp2} ")
