import urllib.request
import datetime
import json

SERVICE_KEY = 'c012adfb7bc42d464b08f43813700d2b3f188cacdf36ad184b403790adaf0ba6'

def getRequestURL(url):
    req = urllib.request.Request(url)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print(f'[{datetime.datetime.now}]request communication success')
            return res.read().decode('utf-8')
        
    except Exception as e:
            print(f'[{datetime.datetime.now}]request communication fail')
            print(f'e:{e}')
            return None
        

def getTourismStatsItem(yyyymm, nat_cd, ed_cd):
    serviceURL = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?"
    parameters += "_type=json&"
    parameters += "serviceKey=" + SERVICE_KEY + '&'
    parameters += "YM=" + yyyymm + '&'
    parameters += "ED_CD=" + ed_cd + '&'
    parameters += "NAT_CD=" + nat_cd

    url = serviceURL + parameters
    res = getRequestURL(url)
    if res == None:
        return None
    else:
        return json.loads(res)
        #json.loads() json형식의 문자열(str)을 파이썬에서 쉽게 사용할 수 있도록 변환함 json --> dict

def getTourismStatsService(nat_cd, ed_cd, nstartYear, nEndYear):
    
    jsonResult = []
    result = []
    natName = ''
    isDataEnd = 0
    dataEND = f'{str(nEndYear)}{str(12)}'
    
    for year in range(nstartYear, nEndYear + 1): #년
        for month in range(1, 13):               #월
            if isDataEnd == 1:
                break

            yyyymm = f'{str(year)}{str(month):0>2}'
            
            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                
                #데이터 끝 확인 코드
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1 #데이터 끝 확인용 flag변수
                    dataEND = f'{str(year)}{str(month-1):0>2}'
                    print('DATA END!')
                    break

                #json data 확인
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace('  ', '')
                num = jsonData['response']['body']['items']['item']['num']
                ed =  jsonData['response']['body']['items']['item']['ed']
                
                jsonResult.append({
                    'nat_name' : natName,
                    'nat_cd' : nat_cd,
                    'yyyymm' : yyyymm,
                    'visit_cnt' : num
                })

    return (jsonResult, natName, ed, dataEND)

def main():

    jsonResult = []
    natName = ''

    print('-----------------------------------------------')
    print('----------국내 입국 외국인 통계 데이터---------')
    print('-----------------------------------------------')

    nat_cd = input('국가 코드 입력[중국(112), 일본(130), 미국(275)]: ')
    nstartYear = int(input('데이터 수집 시작 년도: '))
    nEndYear = int(input('데이터 수집 끝 년도: '))
    ed_cd ='E' # E:입국 D:출국

    jsonResult, natName, ed, dataEND = getTourismStatsService(nat_cd, ed_cd, nstartYear, nEndYear)
    
    if natName == '':
        print('데이터 수집 오류, 담당자에게 문의하세요')
    else:
        print('데이터 수집 성공')
        with open(f'./{natName}_{ed}_{nstartYear}_{dataEND}.json', 'w', encoding='utf-8') as f:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            f.write(jsonFile)




if __name__ == '__main__':
    main()