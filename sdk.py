import requests
from dateutil.parser import parse


class Oura:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.api_url = 'https://api.ouraring.com/v1'


    def __is_date(self, date_str: str, fuzzy=False):
        try:
            parse(date_str, fuzzy=fuzzy)
            return True
        except ValueError:
            return False


    def __make_url(self, endpoint):
        return self.api_url + endpoint


    def __assert_dates(self, dates_list):
        dates_assertion = [self.__is_date(date) for date in dates_list]
        return all(dates_assertion)


    def get_sleep_data(self, start_date: str, end_date: str):
        url = self.__make_url('/sleep')
        assert self.__assert_dates(start_date, end_date), 'A date is invalid!'
        params = {'access_token': self.access_token, 'start' start_date,
                  'end_date': end_date}
        req = requests.get(url, params)
        assert req.status_code == 200, 'An error ocurred in the request!'
        return req.json()['sleep']


    def get_readiness_data(self, start_date: str, end_date: str):
        url = self.__make_url('/readiness')
        assert self.__assert_dates(start_date, end_date), 'A date is invalid!'
        params = {'access_token': self.access_token, 'start': start_date,
                  'end_date': end_date}
        req = requests.get(url, params)
        assert req.status_code == 200, 'An error ocurred in the request!'
        return req.json()['readiness']


    def get_activity_score(self, start_date: str, end_date: str):
        url = self.__make_url('/activity')
        assert self.__assert_date(start_date, end_date), 'A date is invalid!'
        params = {'access_token': self.access_token, 'start': start_date,
                  'end_date': end_date}
        req = requests.get(url, params)
        assert req.status_code == 200, 'An error ocurred in the request!'
        return req.json()['activity']

