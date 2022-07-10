import urllib.request
import json
from statistics import mode
from collections import Counter 
 
def open_url(url):  
    fileobj = urllib.request.urlopen(url)
    fileobj = fileobj.read()
    fileobj = json.loads(fileobj)
    return fileobj
 
whole_api = open_url("https://api.fda.gov/food/enforcement.json?limit=1000")
firms = []
meds = whole_api["results"]
for m in meds:
    firms.append(m["recalling_firm"])
most_common = mode(firms)
occ = (Counter(firms))

print(f"The most common firm in the list is {most_common}, and it appears {max(occ.values())} times")
 
 