from random import random
#Настройки клавиатуры
settings = dict(one_time=False, inline=False)
#Виды CALLBACK кнопок, которые разрешены в сообществе
CALLBACK_TYPES = ('show_snackbar', #Всплывающее сообщение
                  'open_link', #Открыть ссылку
                  'open_app') #Открыть приложение
API_VERSION = '5.131' #Версия API
GROUP_ID = '214168760' #ID Сообщества

#Команды
comands = {
    'search': {'in': ['/search', 'поиск'],
              'out': ['Вот что я нашел'],
              'key': 'search',
              'keyboard': 'search'},
    'next': {'in': ['/next', 'сдедующий'],
              'out': ['Следующий'],
              'key': 'next',
              'keyboard': 'search'},
    'previous': {'in': ['/next', 'предыдущий'],
             'out': ['Предыдущий'],
'key': 'previous',
             'keyboard': 'search'},
    'settings': {'in': ['/settings', 'настройки'],
                'out': ['Настройки'],
'key': 'settings',
                 'keyboard': 'settings'},
    'hello': { 'in': ['/hello', 'привет', 'hello', 'hi', 'privet', 'hey'],
              'out': ['Приветствую', 'Здравствуйте', 'Привет!'],
'key': 'hellow',
              'keyboard': 'menu' },
    'back': { 'in': ['/back', 'назад'],
             'out': ['Назад' ],
'key': 'back',
              'keyboard': 'back'},
    'none': {'in': [],
             'out': ['Не знаю что делать'],
             'keyboard': 'menu'}
}

