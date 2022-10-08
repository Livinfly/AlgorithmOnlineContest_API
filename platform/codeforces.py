import sys
import os

lib_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), os.pardir, os.pardir))
print(lib_path)
sys.path.append(lib_path)

import methods
import json

url = 'https://codeforces.com/api/contest.list'

response = methods.getResponse(url)
content = response.read().decode('utf-8')
content = json.loads(content)
del content["status"]


pos = 0
for i, x in enumerate(content["result"]):
    if x["relativeTimeSeconds"] > 0:
        pos = i
        break
content["result"] = (content["result"][:i])[-1::-1]

content = json.dumps(content)

with open(lib_path + '/contestJson/codeforces.json', 'w') as fp:
    fp.write(content)
    # print(response)
print(content)

'''
  platform
  name
  startTime
  relativeTimeHours
  durationHours
'''
