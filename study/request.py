import requests
import time

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Origin': 'http',
    'Pragma': 'no-cache',
    'Referer': 'http',
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/107.0.0.0Safari/537.36',
    'accept': 'application/json'
}


if __name__ == "__main__":
    while True:
        response = requests.get('http://192.168.46.15/',
                                 headers=headers,
                                 verify=False)
        #print(response.text)
        time.sleep(30)

