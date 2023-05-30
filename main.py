from flask import Flask, jsonify, render_template, request
import requests
import xml.etree.ElementTree as ET
import html
import json

app = Flask(__name__)


# 모든 축제 정보를 요청후 리턴
@app.route('/festivals/<pageNo>')
def view_all(pageNo):
    return get_festivals(pageNo)


def get_festivals(pageNo):
    url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
    params = {
        'serviceKey': 'PH9LodLRmVyqEv1l/OVszYUfRG4OtB21PyMWnlDD/1cf/PSLnO4GONguUMsbMlXDmSMzwHWK4/6YSifuhD5kKA==',
        'pageNo': pageNo,
        'type': 'xml',
    }

    response = requests.get(url, params=params)
    response.encoding = 'utf-8'

    festivalName = []           # 축제이름을 저장하는 배열
    festivalVenue = []          # 개최장소를 저장하는 배열
    fstvlStartDate = []         # 축제시작일를 저장하는 배열
    fstvlEndDate = []           # 축제종료일를 저장하는 배열
    fstvlCo = []                # 축제소개를 저장하는 배열
    location = []               # 축제장소를 저장하는 배열
    address = []


    if response.status_code == 200:
        xml_data = response.text
        root = ET.fromstring(xml_data)

        for item in root.findall('.//item'):

            fstvlNm = item.find('fstvlNm').text             # fsvmlNm 태그의 값을 찾고 값 을  가져온다.
            opar = item.find('opar').text                   # opar 태그의 값을 찾고 값 을  가져온다.
            StartDate = item.find('fstvlStartDate').text    # StartDate 태그의 값을 찾고 값 을  가져온다.
            EndDate = item.find('fstvlEndDate').text        # EndDate 태그의 값을 찾고 값 을  가져온다.
            fstvlComent = item.find('fstvlCo').text         # fstvlComent 태그의 값을 찾고 값 을  가져온다.
            auspcInstt = item.find('auspcInstt').text       # auspcInstt 태그의 값을 찾고 값 을  가져온다.
            rdnmadr = item.find('rdnmadr').text       # auspcInstt 태그의 값을 찾고 값 을  가져온다.

            if(rdnmadr != None):
                decoded_name = html.unescape(rdnmadr)
                address.append(decoded_name)
            else:
                lnmadr = item.find('lnmadr').text  # auspcInstt 태그의 값을 찾고 값 을  가져온다.
                decoded_name = html.unescape(lnmadr)
                address.append(decoded_name)

            decoded_name = html.unescape(fstvlNm)
            festivalName.append(decoded_name)

            decoded_name = html.unescape(opar)
            festivalVenue.append(decoded_name)

            decoded_name = html.unescape(StartDate)
            fstvlStartDate.append(decoded_name)

            decoded_name = html.unescape(EndDate)
            fstvlEndDate.append(decoded_name)

            decoded_name = html.unescape(fstvlComent)
            fstvlCo.append(decoded_name)

            decoded_name = html.unescape(auspcInstt)
            location.append(decoded_name)


            # Convert festivals list to JSON
            # json_data = json.dumps(festivals, ensure_ascii=False)

    return render_template('festivals.html',
                           festivalName=festivalName, festivalVenue=festivalVenue, fstvlStartDate=fstvlStartDate,
                           fstvlEndDate=fstvlEndDate, fstvlCo=fstvlCo, location=location, address=address)


@app.route('/festivals/search')
def search():
    return render_template('test.html')


@app.route('/result', methods=['POST'])
def search_festivals():
    festival_id = request.form.get('id')
    festival_name = request.args.get('fstvn')
    festival_year = request.args.get('fstv')

    return render_template('result.html', festival_id=festival_id)


@app.route('/test')
def index():
    fruits = ['Apple', 'Banana', 'Orange', 'Mango']
    return render_template('test1.html', fruits=fruits)


@app.route('/main')
def h():
    return render_template('test.html')


@app.route('/hello')
def hello():
    name = request.args.get('name')  # 'name' 파라미터 값 가져오기
    age = request.args.get('age')  # 'age' 파라미터 값 가져오기

    return f"Hello, {name}! You are {age} years old."


if __name__ == '__main__':
    app.run()
