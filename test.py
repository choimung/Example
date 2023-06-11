<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fruit = request.form.get('fruit')  # 폼 데이터에서 'fruit' 값을 가져옵니다.

    return render_template('test.html', selected_fruit=fruit)

if __name__ == '__main__':
    app.run()
=======
# from flask import Flask, jsonify, render_template, request
# import requests
# import xml.etree.ElementTree as ET
# import html
#
# app = Flask(__name__)
#
#
# # 페이지 렌더링 부분
# @app.route("/")
# def get_main_form():
#     return render_template("main.html")
#
#
# @app.route('/festivals/<pageNo>')
# def find_festivals_page(pageNo):
#     return get_festivals(pageNo)
#
#
# def init():
#
#
# # api 호출후 요청 결과 가져오기
# # pageno -> 페이지번호
# # fstvlnm -> 축제명
# # year -> 연
# # month -> 월
# # day -> 일
# # insttcode > 기관코드
#
#
# def get_festivals(pageNo="", fstvlName="", year="", month="", day="", insttCode=""):
#     url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
#     params = {
#         'serviceKey': 'PH9LodLRmVyqEv1l/OVszYUfRG4OtB21PyMWnlDD/1cf/PSLnO4GONguUMsbMlXDmSMzwHWK4/6YSifuhD5kKA==',
#         'pageNo': pageNo,
#         'type': 'xml',
#     }
#
#     fstvlName = request.args.get("fstvlName")
#
#     response = requests.get(url, params=params)
#     response.encoding = 'utf-8'
#
#     festivalName = []  # 축제이름을 저장하는 배열
#     festivalVenue = []  # 개최장소를 저장하는 배열
#     fstvlStartDate = []  # 축제시작일를 저장하는 배열
#     fstvlEndDate = []  # 축제종료일를 저장하는 배열
#     fstvlCo = []  # 축제소개를 저장하는 배열
#     location = []  # 축제장소를 저장하는 배열
#
#     # 응답결과가 성공(200) 일때 실행
#     if response.status_code == 200:
#         xml_data = response.text
#         root = ET.fromstring(xml_data)
#
#         for item in root.findall('.//item'):
#             # html 태그의 값을 찾아오고 변수에 값을 저장해준다.
#             fstvlNm = item.find('fstvlNm').text  # fsvmlNm 태그의 값을 찾고 값 을  가져온다.
#             opar = item.find('opar').text  # opar 태그의 값을 찾고 값 을  가져온다.
#             StartDate = item.find('fstvlStartDate').text  # StartDate 태그의 값을 찾고 값 을  가져온다.
#             EndDate = item.find('fstvlEndDate').text  # EndDate 태그의 값을 찾고 값 을  가져온다.
#             fstvlComent = item.find('fstvlCo').text  # fstvlComent 태그의 값을 찾고 값 을  가져온다.
#             auspcInstt = item.find('auspcInstt').text  # auspcInstt 태그의 값을 찾고 값 을  가져온다.
#             rdnmadr = item.find('rdnmadr').text  # auspcInstt 태그의 값을 찾고 값 을  가져온다.
#
#             if fstvlName in fstvlNm:
#                 print("gg")
#                 if (rdnmadr != None):
#                     decoded_name = html.unescape(rdnmadr)
#                     location.append(decoded_name)
#                 else:
#                     lnmadr = item.find('lnmadr').text  # auspcInstt 태그의 값을 찾고 값 을  가져온다.
#                     decoded_name = html.unescape(lnmadr)
#                     location.append(decoded_name)
#
#                 decode_and_append(fstvlNm, festivalName)
#                 decode_and_append(opar, festivalVenue)
#                 decode_and_append(StartDate, fstvlStartDate)
#                 decode_and_append(EndDate, fstvlEndDate)
#                 decode_and_append(fstvlComent, fstvlCo)
#                 decode_and_append(auspcInstt, location)
#             else:
#                 get_festivals(pageNo=str(int(pageNo) + 1), fstvlName=fstvlName, year=year, month=month, day=day,
#                                      insttCode=insttCode)
#
#     return render_template('result.html',
#                            festivalName=festivalName, festivalVenue=festivalVenue, fstvlStartDate=fstvlStartDate,
#                            fstvlEndDate=fstvlEndDate, fstvlCo=fstvlCo, location=location, address=location)
#
#
# def decode_and_append(value, array):
#     decoded_value = html.unescape(value)
#     array.append(decoded_value)
#
#
# if __name__ == '__main__':
#
#     app.run()
#
# # my_list = ["apple", "banana", "orange", "grape"]
# #
# # for i, item in enumerate(my_list):
# #     if "ba" in item:
# #         print("문자열 'ba'가 배열의", i, "번째 인덱스에 위치합니다.")
>>>>>>> edcb8010bf41af5490414fa5fb44c9e358aaea91
