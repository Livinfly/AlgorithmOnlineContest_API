import time
import urllib.request


def getResponse(url):
    cnt = 0
    while True:
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
            }
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
        except:
            print('Error!')
            print('Try to reconnect!')
            time.sleep(600)
            cnt += 1
            if cnt >= 10 :
                break
            continue
        return response
    return -1
