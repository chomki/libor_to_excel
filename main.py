import requests
import pandas as pd
import datetime


시작일='20200101' #실제 keyin필요
종료일='20211231' #실제 keyin필요

시작=datetime.datetime.strptime(시작일,'%Y%m%d') #날짜형식으로 변경
종료=datetime.datetime.strptime(종료일,'%Y%m%d') #날짜형식으로 변경
s=종료-시작 #타임델타형식으로 반환


df=pd.DataFrame()
for i in range(s.days+1):
    조회날짜=시작+datetime.timedelta(i)
    조회날짜= 조회날짜.strftime('%Y%m%d')
    data={'ajax': 'true',
    'tmpInqStrDt': 조회날짜,
    'hid_key_data':'', 
    'inqStrDt': 조회날짜,
    'hid_enc_data':'', 
    'requestTarget': 'searchContentDiv'}
    req = requests.post('https://www.kebhana.com/cms/rate/wpfxd458_05p_01.do',data=data)
    df1 = pd.read_html(req.text)[0]
    df1.set_index('통화코드',inplace=True)
    df1['조회날짜']=조회날짜
    if len(df)==0:
        df=df1
    else:
        df=pd.concat([df,df1])
        


df.to_excel('리보파일.xlsx')
    
