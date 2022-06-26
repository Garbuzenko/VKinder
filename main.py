import json
from pprint import pprint

from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
# from modules.api.ClassVk import ClassVk

from modules.API.ClassVK import ClassVK
from modules.data.data import settings, API_VERSION, GROUP_ID, CALLBACK_TYPES
from modules.keyboard.keyboard import ClassKeyboard
from modules.utils import utils
from modules.utils.utils import get_token


def run_comand(comand, user_id):
    key = comand.get('key')
    if key != 'none':
        print(f'Запустить команду {key}')
        if key == 'next':
            myApi.move_offset(1)
            comand['attachment'] = ','.join(myApi.get_attachments(user_id=user_id))
            pass
        elif key == 'previous':
            myApi.move_offset(-1)
            comand['attachment'] = ','.join(myApi.get_attachments(user_id=user_id))
            pass
        elif key == 'search':
            comand['attachment'] = ','.join(myApi.get_attachments(user_id=user_id))
            pass
    return comand


#Инициализация
offset = 0
f_toggle = True
vk_session = VkApi(token=utils.get_token('VKinder'), api_version=API_VERSION)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=GROUP_ID)
myApi = ClassVK(utils.get_token('access_token'))
print(f"Бот запущен")


# Основной цикл
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:  # Если пришло новое сообщение
        if event.obj.message['text'] != '':
            if event.from_user:
                comand = utils.get_comand(event.obj.message['text'])
                comand = run_comand(comand=comand, user_id=event.object.user_id)
                vk.messages.send(
                    user_id=event.obj.message['from_id'],
                    attachment=comand.get('attachment'),
                    random_id=get_random_id(),
                    peer_id=event.obj.message['from_id'],
                    keyboard=ClassKeyboard.get_keyboard(comand['keyboard']).get_keyboard(),
                    message=utils.get_answer(comand))
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload.get('type') in CALLBACK_TYPES:
            if event.object.payload.get('type') == 'show_snackbar':
                if  'черный' in event.object.payload.get('text'):
                    print('add_black_list')
                    pass
                elif 'избранное' in event.object.payload.get('text'):
                    print('add_favorites')
                    pass
            r = vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data=json.dumps(event.object.payload))
        else:
            #Кастомный тип
            comand = utils.get_comand(event.object.payload.get('type'))
            comand = run_comand(comand=comand, user_id=event.object.user_id)
            print(comand.get('attachment'))
            vk.messages.send(
                user_id=event.object.user_id,
                attachment=comand.get('attachment'),
                random_id=get_random_id(),
                peer_id=event.object.peer_id,
                keyboard=ClassKeyboard.get_keyboard(comand['keyboard']).get_keyboard(),
                message=utils.get_answer(comand))

if __name__ == '__main__':
    print("test")