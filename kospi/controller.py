from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse

class KospiController:
    def __init__(self):
        pass

    def service(self):
        print('1')
        parser = reqparse.RequestParser()
        print('2')
        parser.add_argument('url', type=str, required=True)
        print('3')
        # args = parser.parse_args()
        args = parser.parse_args()
        print('4')
        print('입력된 URL : {}'.format(args.url))
        print('5')
        page = urlopen(args.url)
        soup = BeautifulSoup(page, 'html.parser')
        # print(soup.prettify())
        kospi = soup.find('span', id = 'KOSPI_now')
        return kospi.string