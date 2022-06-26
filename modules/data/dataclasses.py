# 

# Класс определяющий набор данных пользователя ВКонтакте
class VKUserData(object):
    # id пользователя ВКонтакте
    vk_id : int
    # Имя пользователя ВКонтакте
    first_name : str
    # Фамилия пользователя
    last_name: str
    # Дент рождения
    bdate: str
    # Пол пользоветеля
    gender : str
    # id города пользователя
    city_id: str
    # Название города пользователя
    city_title: str
    # адрес траницы ВКонтакте пользователя
    domain: str
    # Дата время последнего общения с ботом
    last_visit: str

    #инициализация класса
    def __init__(self):
        super().__init__()

    vk_id = 0
    first_name = ''
    last_name = ''
    bdate = ''
    gender = ''
    city_id = ''
    city_title = ''
    domain = ''
    last_visit = ''
    # end __init__()

    # вывод данных о пользователе в формате json
    def json():
        pass

# end class VKUserData