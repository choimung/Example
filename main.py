from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET
import html

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/')
def index():
    return f"hello"

@app.route('/festivals')
def search_festivals():
    end_page = 1;
=======
# TODO 홈페이지 주소로 연결할 수 있게 하기
# TODO 검색결과 false시 처리

@app.route('/festivals')
def search_festivals():
>>>>>>> edcb8010bf41af5490414fa5fb44c9e358aaea91
    year = request.args.get('year')
    month = request.args.get('month')
    search = request.args.get('search')

<<<<<<< HEAD
    festivals, search_results = get_festivals(end_page= end_page,search_query=search, year=year, month=month)
    return render_template('festival.html', festivals=festivals, search_results=search_results)

=======
    festivals, search_results = get_festivals(search_query=search, year=year, month=month)
    return render_template('festival.html', festivals=festivals, search_results=search_results)

  #  return render_template('festival.html', festivals=get_festivals(search_query=search,year=year,month=month))
>>>>>>> edcb8010bf41af5490414fa5fb44c9e358aaea91


# 페이지별로 축제정보 렌더링
@app.route('/festivals')
def page_view():
<<<<<<< HEAD
    return render_template('festival.html', festivals=get_festivals(end_page))


def get_festivals(end_page=1, search_query=None, year=None, month=None):
=======
    end_page = 1
    return render_template('festival.html', festivals=get_festivals(end_page))


def get_festivals(end_page=1, search_query=None, location_search=None, year=None, month=None):

>>>>>>> edcb8010bf41af5490414fa5fb44c9e358aaea91
    search_results = False

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
<<<<<<< HEAD
                    # search_results = False
=======
                    search_results = False
>>>>>>> edcb8010bf41af5490414fa5fb44c9e358aaea91
                    continue

                if month and festival_start_year[1] != month:
                    # search_results = False
                    continue

                if search_query and (
                        search_query not in html.unescape(item.find('fstvlNm').text)
                        and search_query not in html.unescape(
                    item.find('rdnmadr').text or item.find('lnmadr').text).replace(" ", "")
                ):
                    continue

                festival = {
                    'name': html.unescape(item.find('fstvlNm').text),
                    'location': html.unescape(item.find('opar').text),
                    'start_date': html.unescape(item.find('fstvlStartDate').text),
                    'end_date': html.unescape(item.find('fstvlEndDate').text),
                    'description': html.unescape(item.find('fstvlCo').text),
                    'venues': html.unescape(item.find('rdnmadr').text or item.find('lnmadr').text),
                    'url': html.unescape(item.find('homepageUrl').text or '')
                }
                festivals.append(festival)
                search_results = True

    return festivals, search_results


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
    app.run(host='0.0.0.0')