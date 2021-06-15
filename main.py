import requests
import os
from pprint import pprint


# У Яндекс.Диска есть очень удобное и простое API.
# Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет
# на Яндекс.Диск с таким же именем.
#
#     Все ответы приходят в формате json;
#     Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
#     Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
#

TOKEN = 'AAAAAAA'


def get_headers():
    return {
        'Accept': 'application/json',
        'Authorization': TOKEN
    }


def get_upload_link():
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    filename = '/' + os.path.basename(file_path)
    params = {'path': filename, 'overwrite': 'true'}
    response = requests.get(upload_url, params=params, headers=get_headers())
    upload_link = response.json().get('href')
    return upload_link


def upload(file_path):
    """Функция загружает файл file_path на яндекс диск"""
    files = {'file': open(file_path, 'rb')}
    headers = get_headers()
    response = requests.put(get_upload_link(), files=files, headers=headers)
    response.raise_for_status()
    if response.status_code == 201:
        print('Файл загружен на Я.Диск')
    return 'Файл загружен'


file_path = r'c:\my_folder\file.txt'
upload(file_path)
