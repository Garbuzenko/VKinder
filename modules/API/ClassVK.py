from pprint import pprint

import requests


class ClassVK(object):
    API_URL = 'https://api.vk.com/method/'

    def __init__(self, access_token=None):
        self.access_token = access_token
        self.offset = 0 #Сдвиг для поиска
    @staticmethod
    def sex_invert(sex):
        if sex == 1:
            sex = 2
        elif sex == 2:
            sex = 1
        else:
            sex = 0
        return sex
    def move_offset(self, i):
        self.offset += i
    def set_offset(self, i):
        self.offset = i

    def search(self, user_id, offset, count):
        params = self.get_info(user_id)
        search_list = self.users_search(params, count=count, offset=offset)
        pprint(search_list)
        return search_list
    def get_user_data(self, id, offset):
        attachments = []
        content = ''
        if id != 0:
            params = self.get_info(id)

            content = f'\n{params.get("first_name")} {params.get("last_name")}'
            self.get_info(id)  # Параметры пользователя

            photos = self.photos_get(id, 3)
            if photos.get('response') is not None:
                items = photos['response']['items']
                for item in items:
                        attachments.append(f'photo{id}_{item.get("id")}')
        return [','.join(attachments), content]
    def users_search(self, params, count=1, offset=0):
        # [_city, _bdate, _sex] = params

        method = 'users.search'
        url = self.API_URL + method
        params = {
            'count': count,
            'city': params.get("city").get("id"),
            'offset': offset,
            # 'bdate': _bdate,
            'sex': self.sex_invert(params.get("sex")),
            'access_token': self.access_token,
            'v': '5.131'
        }

        # print(method ,params)
        res = requests.get(url, params=params)
        response = res.json().get("response")
        # print(response)
        # Надо получить
        ids = []
        for r in response.get('items'):
            # print(r)
            ids.append(r.get("id"))
        return ids

    def get_info(self, user_ids):
        method = 'users.get'
        url = self.API_URL + method
        params = {
            'user_ids': user_ids,
            'access_token': self.access_token,
            'fields': 'screen_name, city, bdate, sex',
            'v': '5.131'
        }
        res = requests.get(url, params=params)
        response = res.json().get("response")
        for r in response:
            res = r
            # print(r)
            # _city = r.get("city").get("id")
            # _bdate = r.get("bdate")
            # _sex = r.get("sex")
            break
        return res#[_city, _bdate, _sex]

    def get_id(self, user_ids):
        method = 'users.get'
        url = self.API_URL + method
        params = {
            'user_ids': user_ids,
            'access_token': self.access_token,
            'v': '5.131'
        }
        res = requests.get(url, params=params)
        response = res.json().get("response")
        _id = 0
        print(response)
        for r in response:
            _id = r.get("id")
            break
        return _id

    @staticmethod
    def get_max_url(item):
        max_height = -1
        res = ""
        for s in item['sizes']:
            if s['height'] > max_height:
                max_height = s['height']
                res = s['url']
        return res

    def photos_get(self, owner_id: str, count=3):
        method = 'photos.get'
        url = self.API_URL + method
        params = {
            'owner_id': owner_id,
            'album_id': 'profile',
            'access_token': self.access_token,
            'extended': 1,
            'count': count,
            'v': '5.131'
        }
        res = requests.get(url, params=params).json()

        if res.get('error') is not None:
            print(res['error']['error_msg'])

        return res
