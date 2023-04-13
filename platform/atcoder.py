import sys
import os

lib_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), os.pardir, os.pardir))
print(lib_path)
sys.path.append(lib_path)

from bs4 import BeautifulSoup
import json
import methods

url = 'https://atcoder.jp/contests/?lang=en'

response = methods.getResponse(url)
<<<<<<< HEAD
if response != -1 :

    content = response.read().decode('utf-8')

    soup = BeautifulSoup(content, 'lxml')

    # print(soup)

    contestList = {"result": []}

    platform = 'atcoder'

    content = soup.select('#contest-table-upcoming tbody tr')
    for contest in content:
        t = contest.find('time').get_text()[:-8]
        startTime = t[:-5] + str(int(t[-5:-3]) - 1) + t[-3:]
        name = contest.select('td')[1].find('a').get_text()
        durationHours = contest.select('td')[2].get_text()
        contestList["result"].append({
            "platform": platform,
            "name": name,
            "startTime": startTime,
            "durationHours": durationHours
        })
        # print(platform, startTime, name, durationHours)
    with open(lib_path + '/contestJson/atcoder.json', 'w') as fp:
        json.dump(contestList, fp)

    print(contestList)


'''
platform
name
startTime
*relativeTimeHours
durationHours
'''
=======
content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

# print(soup)

contestList = {"result": []}

platform = 'atcoder'

content = soup.select('#contest-table-upcoming tbody tr')
for contest in content:
    t = contest.find('time').get_text()[:-8]
    startTime = t[:-5] + str(int(t[-5:-3]) - 1) + t[-3:]
    name = contest.select('td')[1].find('a').get_text()
    durationHours = contest.select('td')[2].get_text()
    contestList["result"].append({
        "platform": platform,
        "name": name,
        "startTime": startTime,
        "durationHours": durationHours
    })
    # print(platform, startTime, name, durationHours)
with open(lib_path + '/contestJson/atcoder.json', 'w') as fp:
    json.dump(contestList, fp)

print(contestList)


# print(contest_list)

'''
  platform
  name
  startTime
  relativeTimeHours
  durationHours
'''
>>>>>>> 2d053721b6b5d3d6235aafe3e9a71c7beb5738dc
