from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET
import html

app = Flask(__name__)

# TODO 홈페이지 주소로 연결할 수 있게 하기


# 페이지별로 축제정보 렌더링
@app.route('/festivals')
def page_view():
    end_page = 2
    return render_template('festival.html', festivals=get_festivals(end_page))


def get_festivals(end_page, search_query=None, location_search=None, year=None, month=None):
    url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
    festivals = []

    for page in range(1, end_page + 1):
        params = {
            'serviceKey': 'PH9LodLRmVyqEv1l/OVszYUfRG4OtB21PyMWnlDD/1cf/PSLnO4GONguUMsbMlXDmSMzwHWK4/6YSifuhD5kKA==',
            'pageNo': page,
            'type': 'xml',
        }
        response = requests.get(url, params=params)
        response.encoding = 'utf-8'

        if response.status_code == 200:
            xml_data = response.text
            root = ET.fromstring(xml_data)

            for item in root.findall('.//item'):
                festival_start_year = html.unescape(item.find('fstvlStartDate').text).split("-")
                if year and festival_start_year[0] != year:
                    continue

                if month and festival_start_year[1] != month:
                    continue

                festival_name = html.unescape(item.find('fstvlNm').text)
                if search_query and search_query.lower() not in festival_name.lower():
                    continue

                festival_location = html.unescape(item.find('rdnmadr').text or item.find('lnmadr').text)
                if location_search and location_search not in festival_location:
                    continue

                festival = {
                    'name': html.unescape(item.find('fstvlNm').text),
                    'location': html.unescape(item.find('opar').text),
                    'start_date': html.unescape(item.find('fstvlStartDate').text),
                    'end_date': html.unescape(item.find('fstvlEndDate').text),
                    'description': html.unescape(item.find('fstvlCo').text),
                    'venues': html.unescape(item.find('rdnmadr').text or item.find('lnmadr').text)
                }
                festivals.append(festival)

    return festivals


# def get_festivals(page_number, search_query=None, year = '2023'):
#
#     url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
#     params = {
#         'serviceKey': 'PH9LodLRmVyqEv1l/OVszYUfRG4OtB21PyMWnlDD/1cf/PSLnO4GONguUMsbMlXDmSMzwHWK4/6YSifuhD5kKA==',
#         'pageNo': page_number,
#         'type': 'xml',
#     }
#     response = requests.get(url, params=params)
#     response.encoding = 'utf-8'
#
#     festivals = []
#
#     if response.status_code == 200:
#         xml_data = response.text
#         root = ET.fromstring(xml_data)
#
#         for item in root.findall('.//item'):
#
#             festival_start_year = html.unescape(item.find('fstvlStartDate').text).split("-")
#             if festival_start_year[0] != year:
#                 continue
#
#             festival_name = html.unescape(item.find('fstvlNm').text)
#             if search_query and search_query.lower() not in festival_name.lower():
#                 continue
#
#             festival = {'name': html.unescape(item.find('fstvlNm').text),
#                         'location': html.unescape(item.find('opar').text),
#                         'start_date': html.unescape(item.find('fstvlStartDate').text),
#                         'end_date': html.unescape(item.find('fstvlEndDate').text),
#                         'description': html.unescape(item.find('fstvlCo').text),
#                         'venues': html.unescape(item.find('rdnmadr').text or item.find('lnmadr').text)
#                         }
#
#             festivals.append(festival)
#
#     return festivals


if __name__ == '__main__':
    app.run()
