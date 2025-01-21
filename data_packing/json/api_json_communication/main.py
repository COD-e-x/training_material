import requests
import json

# # URL для взаимодействия с API
# url = 'https://jsonplaceholder.typicode.com/posts'
#
# data = {
#     'title': 'foo',
#     'body': 'bar',
#     'userID': 1
# }
#
# response = requests.post(url, json=data)
#
# if response.status_code == 201:
#     print('Данные успешно отправлены!')
#     response_data = response.json()
#     print(f'Ответ от сервера: {json.dumps(response_data, indent=4)}')
# else:
#     print(f'Ошибка! Статус кода: {response.status_code}')
#
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     print('Данные успешно получены!')
#     posts = response.json()
#     print(f'Количество постов: {len(posts)}')
#     print(json.dumps(posts[:2], indent=4))
# else:
#     print(f'Ошибка! Статус кода: {response.status_code}')


url = 'https://api.github.com/users/COD-e-x/repos'

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    print(f'Количество репозиториев: {len(repos)}')
    for repo in repos:
        print(f'Репозиторий: {repo['name']}')
else:
    print(f'Ошибка! Статус кода: {response.status_code}')
