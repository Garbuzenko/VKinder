# Пол пользователя ВКонтакте
VK_MALE = 2
VK_FEMALE = 1
VK_UNKNOWN_GENDER = 0

# Класс определяющий набор данных пользователя ВКонтакте
class VKUserData(object): 
    # id пользователя ВКонтакте
    vk_id : int
    # Имя пользователя ВКонтакте
    first_name : str
    # Фамилия пользователя
    last_name: str
    # День рождения пользователя
    bdate: str
    # Пол пользоветеля
    gender : str
    # id города пользователя
    city_id: int
    # Название города пользователя
    city_title: str
    # адрес траницы ВКонтакте пользователя
    domain: str
    # Дата время последнего общения с ботом
    last_visit: str

    #инициализация класса
    def __init__(self):
        super().__init__()

        self.vk_id = 0
        self.first_name = ''
        self.last_name = ''
        self.bdate = ''
        self.gender = ''
        self.city_id = 0
        self.city_title = ''
        self.domain = ''
        self.last_visit = ''
    # end __init__()

    # вывод данных о пользователе в формате json
    def json():
        pass

# end class VKUserData
