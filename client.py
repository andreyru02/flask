import requests


# resp = requests.get('http://127.0.0.1:5000/advertisement').json()
# print(resp)


# resp = requests.get('http://127.0.0.1:5000/advertisements/1').json()
# print(resp)


# resp = requests.post('http://127.0.0.1:5000/advertisements/',
#                      json={
#                          'title': 'test title',
#                          'descriptions': 'test descriptions',
#                          'create_date': '2021-09-23',
#                          'owner': 1
#                      }).json()
# print(resp)

resp = requests.delete('http://127.0.0.1:5000/advertisements/1').json()
print(resp)