import urllib.request
import datetime
import json
import urllib.parse

client_id = '7QXnRoUfcyfpRCERY4_G'
client_secret = 'QFqa8DYeGh'

#naver에서 데이터 가져옴
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQEST SUCCESS!!')
            # print(f'response data: {response.read().decode('utf-8')}')
            #decode 바이트 코드를 문자열로 변환하는 것
            return response.read().decode('utf-8')
    except Exception as e:
        print(f'[{datetime.datetime.now()}]Error : {e}')
        return None

#naver에서 데이터 검색
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json' #news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)
   
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)
    
def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt': cnt,
        'title' : title,
        'description' : description,
        'org_link' : org_link,
        'link' : link,
        'pDate' : pDate
    })

def main():
    node = 'news'  #크롤링 대상 지정
    srcText = input('검색어 입력: ')
    cnt = 0 #검색량 제한
    jsonResult = []   #json -데이터를 주고받는 형식

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')

    while jsonResponse != None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)
            
        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    with open(f'{srcText}_naver_{node}.json','w',encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)


if __name__ == '__main__':
    main()