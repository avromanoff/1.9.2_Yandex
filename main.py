import requests
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
# HOST: https://cloud-api.yandex.net:443
# Token: AQAAAAAAjy47AADLW5Zh73ErEEgrokZtbf6PU8c
# ID: 86c3ae93dfe14892ac93fbfa36e5f830
# Пароль: 7f93167989fc46bd94f0e94241b814fc
token = 'AQAAAAAAjy47AADLW5Zh73ErEEgrokZtbf6PU8c'

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth{}.format(self.token)'
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resourses/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json()) # удалить, смотрю результат запроса пути
        return response.json()

    def upload(self, file_path, filename):
        """Метод загружает файл file_path на яндекс диск"""
        # Тут ваша логика
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')
        # with open ("C:\test\test.txt", 'rb') as f:
        #     resp = requests.post('ya.ru', files={"file": f})
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('AQAAAAAAjy47AADLW5Zh73ErEEgrokZtbf6PU8c')
    # result = uploader.upload("c:\my_folder\file.txt")
    # pprint(YaUploader.upload(r"c:\my_folder\file.txt", "file.txt"))
    print(uploader.upload('file.txt', r"c:\my_folder\file.txt"))


