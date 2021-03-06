# Командный проект по курсу «Профессиональная работа с Python»

## VKinder

### Установка
Перед запуском нужно создать файл D:\token\tokens.json со структурой
{"VKinder": "Токен группы","db_connection": "mysql+pymysql://ИМЯ:ПАРОЛЬ@ХОСТ:ПОРТ/ИМЯ", "access_token": "токен пользователя"}

Токен пользователя можно получить по ссылке https://oauth.vk.com/authorize?client_id=8116853&scope=wall,offline&redirect_uri=https://cosmio.io/api/vkinder/api.php&display=page&v=5.24&response_type=token

### Цель проекта

Разработать программу-бота для взаимодействия с базами данных социальной сети. Бот будет предлагать различные варианты людей для знакомств в социальной сети Вконтакте в виде диалога с пользователем.

Выполнены задачи:
- Спроектирована база данных (БД) для программы
- Создано сообщество ВК https://vk.com/club214168760 в диалогах которого живет Бот
- Разработана программа-бота на Python с алгоритмом:
1. Используя информацию (возраст, пол, город) о пользователе, который общается с ботом в ВК, производится поиск других людей (других пользователей ВК) для знакомств.
2. У тех людей, которые подошли под критерии поиска, получить три самые популярные фотографии в профиле. Популярность определяется по количеству лайков.
3. Выводить в чат с ботом информацию о пользователе в формате: ФИО, Ссылка, Фото
4. Реализовано меню "Следующий", "Предыдущий".
5. Подгрузка пользователей осуществляется пакетами по N человек с записью в базу данных, когда данные в БД заканчиваются, осуществляется подгрузка следующих N пользователей
Этот функционал позволяет обойти ограничение в поиске 1000 человек, так как используется смещение OFFSET и ограничение выборки COUNT
6. Реализованы кнопки "Добавить в избранное" и "Показать избранные"
7. Реализованы кнопки "Добавить в черный список" и "Показать черный список". Человек из черного списка пропускается
8. Реализована возможность получения токена от пользователя с нужными правами.
9. Созданы кнопки в чате для взаимодействия с ботом.

## Техническое описание проекта

### Структура каталога проекта

- main.py
- requirements.txt
- README.md
  - docs
  - modules
    - API
        - ClassVK.py
    - data
        - data.py
    - db
      - dataclasses.py
      - databases.py
      - db.sql
    - keyboard
      - keyboard.py
    - logic
      - logic.py
    - utils
      - utils.py
  - token
    - token.json
  
### Модуль main.py

>Главный модуль программы main.py

>В этом модуле происходит инициализация всех подсистем проекта и реализован главный цикл обработки событий,

>на которые реагирует Бот ВКонтакте.

### Модуль ClassVK.py
>В модуле определяется класс ClassVK реализующий логику взаимодействия с API ВКонтакте, для

>работы Бота.

### Модуль data.py
>Вспомогательные наборы данных для работы интерфейса Бота ВКонтаке

### Модули db

>Файл db.sql - содержит скрипт инициализации базы данных проекта

>Файл dataclasses.py - содержит опредеделение основного класса данных проекта VKUserData

>Файл databases.py - определяет класс DataBase для работы с базой данных проекта

### Модуль keyboard.py
>Определяет вспомогательные класс class ClassKeyboard: для взаимодействия Бота с Пользователем

### Модуль logic.py
>Определяет класс "логики" проекта class Logic(object). 

>Класс loguc.py служит своеобразным интерфейсом между базой данных проекта и обработчиком событий.

### Модуль utils.py
>Содержит вспомогательные функции, такие как загрузку токена из файла с параметрами проекта.

### Папка token
>Содержит файл token.json: основные параметры проекта - токены для работы Бота и строку сединения с Базой данных.
