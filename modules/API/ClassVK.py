import requests


class ClassVK(object):
    API_URL = 'https://api.vk.com/method/'

    def __init__(self, access_token=None):
        self.access_token = access_token
        self.offset = 0
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
    def get_attachments(self, user_id):
        params = self.get_info(user_id)  # Параметры пользователя
        search_list = self.users_search(params)
        for l in search_list:
            attachments = []
            photos = self.photos_get(l, 3)
            if photos.get('response') is not None:
                items = photos['response']['items']
                for item in items:
                    attachments.append(f'photo{l}_{item.get("id")}')
        return attachments
    def users_search(self, params, count=1):
        [_city, _bdate, _sex] = params

        method = 'users.search'
        url = self.API_URL + method
        params = {
            'count': count,
            'city': _city,
            'offset': self.offset,
            # 'bdate': _bdate,
            'sex': self.sex_invert(_sex),
            'access_token': self.access_token,
            'v': '5.131'
        }
        print(method ,params)
        res = requests.get(url, params=params)
        response = res.json().get("response")
        print(response)
        # Надо получить
        ids = []
        for r in response.get('items'):
            print(r)
            ids.append(r.get("id"))
        return ids

    def get_info(self, user_ids):
        method = 'users.get'
        url = self.API_URL + method
        print(self.access_token)
        params = {
            'user_ids': user_ids,
            'access_token': self.access_token,
            'fields': 'city, bdate, sex',
            'v': '5.131'
        }
        res = requests.get(url, params=params)
        response = res.json().get("response")
        for r in response:
            print(r)
            _city = r.get("city").get("id")
            _bdate = r.get("bdate")
            _sex = r.get("sex")
            break
        return [_city, _bdate, _sex]

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
