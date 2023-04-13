import sys
import os

lib_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), os.pardir, os.pardir))
print(lib_path)
sys.path.append(lib_path)

<<<<<<< HEAD
from config import *
import time
import methods
import json, hashlib

curTime = str(int(time.time()))
sha = 'RoTarn/contest.list?apiKey='+codeforceApiKey+'&gym=false&time='+curTime+'#'+codeforceApiSecret
shaRes = hashlib.sha512()
shaRes.update(sha.encode('utf-8'))
shaRes = shaRes.hexdigest()
url = 'https://codeforces.com/api/contest.list?gym=false'
url += '&apiKey='+codeforceApiKey+'&time='+curTime+'&apiSig=RoTarn'+shaRes
# print(url)

response = methods.getResponse(url)

if response != -1 :
    
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
*relativeTimeHours
durationHours
'''
=======
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
>>>>>>> 2d053721b6b5d3d6235aafe3e9a71c7beb5738dc
