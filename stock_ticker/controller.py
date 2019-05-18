from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse

class Stock_ticketrController:
    def __init__(self):
        pass

    def service(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ticker', type=str, required=True)
        args = parser.parse_args()
        print('입력된 종목코드 : {}'.format(args.ticker))
        url='https://finance.naver.com/item/main.nhn?code=005930'+args.ticker
        page = urlopen(args.url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.prettify())
        kospi = soup.find('span', id = 'KOSPI_now')
        return ''