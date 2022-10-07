import time
import urllib.request


def getResponse(url):
    while True:
        try:
            response = urllib.request.urlopen(url)
        except:
            print('Error')
            time.sleep(10)
            continue
        return response
