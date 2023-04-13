import sys
import os

lib_path = os.path.abspath(os.path.join(
    os.path.abspath(__file__), os.pardir, os.pardir))
print(lib_path)
sys.path.append(lib_path)

from bs4 import BeautifulSoup
import json
import methods

urls = [
    'https://ac.nowcoder.com/acm/contest/vip-index?topCategoryFilter=13',
    # 'https://ac.nowcoder.com/acm/contest/vip-index?topCategoryFilter=14',
]

contestList = {"result": []}

for url in urls :
    response = methods.getResponse(url)
    if response != -1 :

        content = response.read().decode('utf-8')

        soup = BeautifulSoup(content, 'lxml')

        # print(soup)

        platform = 'nowcoder'

        content = soup.select('div[class="platform-item js-item"] div[class="platform-item-cont"]')
        # print(content)
        for contest in content:
            t = contest.select('li[class="match-time-icon"]')[0].get_text()
            p = t.find('时长:')+3
            tt = t[p:-1]

            length, pDay, pHour, pMinute = 0, tt.find('天'), tt.find('小时'), tt.find('分钟')

            if pDay != -1 :
                length += int(tt[:pDay])*24*60
            if pHour != -1 :
                length += int(tt[pDay+1:pHour])*60
            if pMinute != -1 :
                length += int(tt[pHour+2:pMinute])
            
            hh, mm = length//60, length%60

            startTime = contest.select('li[class="match-time-icon"]')[0].get_text()[9:25]
            name = contest.select('a')[0].get_text()
            durationHours = str(hh).rjust(2, '0')+':'+str(mm).rjust(2, '0')
            contestList["result"].append({
                "platform": platform,
                "name": name,
                "startTime": startTime,
                "durationHours": durationHours
            })
            # print(platform, startTime, name, durationHours)

with open(lib_path + '/contestJson/nowcoder.json', 'w') as fp:
    json.dump(contestList, fp)

print(contestList)

'''
platform
name
startTime
*relativeTimeHours
durationHours
'''