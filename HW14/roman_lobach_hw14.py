# Подключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ), отримайте теперішній курс валют и запишіть його в TXT-файл в такому форматі:
#  "[дата, на яку актуальний курс]"
# 1. [назва валюти 1] to UAH: [значення курсу валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу валюти n]
#
#
# опціонально передбачте для користувача можливість обирати дату, на яку він хоче отримати курс
#
#
#
# P.S.  За можливості зробіть все за допомогою ООП


import requests
import re


class GetRequest:
    def __init__(self, base_url, endpoint='', param=''):
        self.url = {
            'base_url': base_url,
            'endpoint': endpoint,
            'param': param
        }

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        """
            method forms url

            Args:
                value (dict): dict with base url, endpoint and date
        """

        if value['endpoint'] and value['param']:
            self._url = value['base_url'] + value['endpoint'] + value['param']
        else:
            self._url = value['base_url']

    @property
    def response(self):
        """
            method forms request

            Returns:
                value (dict): dict with status and response
        """
        try:
            response = requests.get(self.url)
            print('status', response.status_code)

            if 100 < response.status_code < 300 and response.json():
                return {
                    'status': 'ok',
                    'response': response.json()
                }
            else:
                return {
                    'status': 'err',
                    'response': f'\nSorry, something went wrong. Status code {response.status_code}.\n'
                                f'Data is {"empty" if not response.json() else response.json()}\n'
                }

        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")
            return {
                'status': 'err',
                'response': f"\nAn error occurred: something wrong with ethernet connection or url.\n"
            }


class DataTemplateNBU:
    def __init__(self, data):
        self.template = data

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        """
            method parse response

            Args:
                value (dict): dict with status and response
        """

        if value['status'] == 'err':
            print('from like error')
            self._template = value['response']

        else:
            raw_data = value['response']
            header = f'Valid date: {raw_data[0]["exchangedate"]}\n'
            body = ''

            for index, exchange_block in enumerate(raw_data):
                body = body + f'{index + 1}. {exchange_block["cc"]} to UAH: {exchange_block["rate"]}₴\n'

            self._template = header + body + '\n'


class ResponseDataSaver:
    output_file_name = None
    data = None

    def __init__(self, output_file_name, data):
        self.output_file_name = output_file_name
        self.data = data

    def save(self):
        with open(self.output_file_name, "a") as file:
            file.write(self.data)


class ExchangeInterface:

    @staticmethod
    def get_date():
        user_date = ''

        while not user_date:
            user_date = input('If you want to get the exchange rate for a specific date, please enter it in YYYYMMDD format.\n'
                              'If you want to get the rate for today, leave this input blank here: ').strip()

            if not user_date:
                return user_date

            try:
                if bool(re.match("^[0-9]+$", user_date)) and len(user_date) == 8:
                    return user_date
            except:
                print('Sorry! You entered wrong data format. Try again, please')

    def run_nbu_exchange_saver(self):
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        date_end_point = '&date='
        date = self.get_date()

        received_data = GetRequest(url, date_end_point, date)
        prepared_data = DataTemplateNBU(received_data.response)
        ResponseDataSaver('exchange.txt', prepared_data.template).save()


ExchangeInterface().run_nbu_exchange_saver()
