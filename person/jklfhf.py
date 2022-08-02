# import psycopg2
# from psycopg2 import OperationalError
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#
# a = 'testperson'
#
#
# def create_connection(db_name, db_user, db_password, db_host, db_port):
#     connection = None
#     try:
#         connection = psycopg2.connect(
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print('Connection to PosrgresQL DB successfull')
#         cursor = connection.cursor()
#         # print(connection.get_dsn_parameters(), "\n")
#         # Выполнение SQL-запроса
#         cursor.execute(
#             "SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog')")
#         # Получить результатn
#         for x in cursor:
#             print(x)
#         #Получить результат
#         # cursor.execute("SELECT * from django_content_type")
#         # record = cursor.fetchall()
#         # for i in record:
#         #     print("django_content_type", i)
#
#         # cursor.execute("DROP TABLE person_contactfacebook")
#         # connection.commit()
#         # cursor.execute("DELETE FROM django_content_type WHERE id='18'")
#         # connection.commit()
#
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#     return connection
# #
# #
# # # con = create_connection("DB1", "postgres", "root", "127.0.0.1", "5432")
# con = create_connection("ddsdcob9bgai0s", "cxykdjoiuitbnk", "3a2732e3887fb34b436a8e23280163338bbb879fe0e4a4371dca48d5eae472e1",
#                         "ec2-54-152-28-9.compute-1.amazonaws.com", "5432")
#
#
# def execute_query_users(connection):
#     users = [
#         ("Col", "Cam"),
#     ]
#     user_records = ", ".join(["%s"] * len(users))
#     insert_query = (
#         f"INSERT INTO test (name, last_name) VALUES {user_records}"
#     )
#     connection.autocommit = True
#     cursor = connection.cursor()
#     cursor.execute(insert_query, users)
#
#
# execute_query_users(con)
#
#
# # def create_table(connection, query):
# #     connection.autocommit = True
# #     cursor = connection.cursor()
# #     try:
# #         cursor.execute(query)
# #     except OperationalError as e:
# #         print(f"The error '{e}' occurred")
# #
# # create_test_table = """
# # CREATE TABLE IF NOT EXISTS test (
# #   id SERIAL PRIMARY KEY,
# #   name VARCHAR(100),
# #   last_name VARCHAR(100)
# # )
# # """
# #
# # create_table(con, create_test_table)

# a = {'name': 'vasia', 'last': 'kim'}
# c = [v for k, v in a.items()]
# c = [tuple(c)]
# print(c)

# def dec_func(func):
#     def wrapper(*args):
#         print(args)
#         for i in args:
#             print(i * 5)
#
#         func(*args)
#
#     return wrapper
#
#
# @dec_func
# def test_fun(x, y, z):
#     pass
#
#
# test_fun(4, 5, 6)
# def big_dec(a, b):
#     print('Big_dec', a + b)
#
#     def dec_func(func):
#         print('dec_func', a * b)
#
#         def wrapper(*args):
#             for i in args:
#                 print('Умножим аргументы: ', i * 5)
#             print('Это из big_dec', a * 2, b * 2)
#             func(*args)
#
#         return wrapper
#
#     return dec_func
#
#
# @big_dec(5, 6)
# def new_fun(a, b, c):
#     pass


# new_fun(1, 2, 3)
# import datetime
# import time
#
# a = ('Alex6', 'Alex6', 'dada@6mail.com', '+375291811450')
# b = datetime.datetime.now()
# a = a + (str(b),)

# b = [[0 for _ in range(5)] for _ in range(5)]
# for i in b:
#     print(*i)

# import jwt
# jwt_fb = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImJmMWMyNzQzYTJhZmY3YmZmZDBmODRhODY0ZTljMjc4ZjMxYmM2NTQiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoi0KjQsNC70LjQvNC-INCd0LjQutC40YLQsCIsInBpY3R1cmUiOiJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDM1OTQ5NTI0MzkwNTIvcGljdHVyZSIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS96bnMtYXV0aCIsImF1ZCI6Inpucy1hdXRoIiwiYXV0aF90aW1lIjoxNjU4Mzk4MTI4LCJ1c2VyX2lkIjoiOHNxd3puU2RFZ2dxM0hOcEd3ZmtXTmJyRDBkMiIsInN1YiI6IjhzcXd6blNkRWdncTNITnBHd2ZrV05ickQwZDIiLCJpYXQiOjE2NTgzOTgxMjgsImV4cCI6MTY1ODQwMTcyOCwiZW1haWwiOiJtZWdhZnJvc3RiYWxsQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJmYWNlYm9vay5jb20iOlsiMTAzNTk0OTUyNDM5MDUyIl0sImVtYWlsIjpbIm1lZ2Fmcm9zdGJhbGxAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZmFjZWJvb2suY29tIn19.TmhKNZu1uGDrzwuAiiDaMQTVSk9A_d4fGi_6q4-Nj2p4-dz1IZlELmf9D0mAXnX4Ik98sR3gsBMiJbwWwx4m8WMD_pjWP_Pox9LgiLIgqJVYw2U4nuhr3QwOC5gSImS-j2aNHGK-mFS0hYZN6pWxCOxs9J2VKaAgSjmqtIKMF1hQgyp0TB41F67ORUgcT2D38eqL8zPaOXDDr_Q_tq600kl6D35Fz7-QyCQ3VhTP1OdTZx9ac7KTMjDtfoXXUWCqaIKwBrWQFczKv-T8Z_jFzSFABJ2EquPzP99Sq8Y-OjpKu6Ru32-JJphvuINLlyeGukA7jkijQmoUEoxDQQaEDQ'
# __jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyMVRaNkI1RUItWUgyR0hqYlhNRFktdGVPQ3dwS2ZaR0FpZjhESkI2VDBzIn0.' \
#         'eyJleHAiOjE2NTc3MzkzNDAsImlhdCI6MTY1NzczOTA0MCwianRpIjoiMDUwN2U0NjAtNzhjYi00YzgzLWFhMmUtNzdjNzcyYjAxOGZjIiwiaXNzIj' \
#         'oiaHR0cHM6Ly9pZC5waXhvbW5pYS5jb20vcmVhbG1zL2RlZmF1bHQiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOWY3NjNjOGEtODc5MC00NTc0LTg5Nzc' \
#         'tYzA4NjgxN2Y4OTQ3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoicGl4b21uaWEtYXBwLWlvcyIsInNlc3Npb25fc3RhdGUiOiJhM2QzYWRhMy0zODA3LTQ1' \
#         'ZmUtODczNS00ODFmNWFiYzZjYTUiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwiZGVmYXVsdC1yb2xlcy' \
#         '1kZWZhdWx0IiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbInZpZXctYXBwbGljYXRpb25z' \
#         'Iiwidmlldy1jb25zZW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiYTNkM2FkYTMtMzgwNy00NWZlLTg' \
#         '3MzUtNDgxZjVhYmM2Y2E1IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoicGl4b21uaWEgcGl4b21uaWEiLCJwcmVmZXJyZWRfdXNlcm5hbWU' \
#         'iOiJwaXhvbW5pYWRldkBnbWFpbC5jb20iLCJnaXZlbl9uYW1lIjoicGl4b21uaWEiLCJmYW1pbHlfbmFtZSI6InBpeG9tbmlhIiwiZW1haWwiOiJwaXh' \
#         'vbW5pYWRldkBnbWFpbC5jb20ifQ.ePCga8iaqAtiB5AvGtSFii4nz70J4mzdRvpbrI064_4sJrje2oWn15-Sg9OsCEzkUYVah9a8obYvccUE_ASkfpRZH' \
#         'rlgTseKksw4hynuKX17Kjw_uQKdWAEemJoEpFTtzj7SOBezEC7vhKl0EELSvcJ4AcWtp2Wosego0EDfy-LO_160-BpMyuZZG-vTw0jVTmhfjwOkmoeae' \
#         'us0q6D6LBZt9ntUpsdXBXRq-CmAB8AI9TN1_Y1Jx7BU0tWkQ3RtTyISiNvMK8PyWQibZwcJe7iA0YHwK_hfpYNVTj5dPbCrBev0neAICA85Z3gWPGCNmS' \
#         'kTng0MPzaqiv15ld68uw'

# decoded = jwt.decode(jwt_fb, options={"verify_signature": False})
# print(decoded)
# email = decoded['email']
# username = decoded['name']
# print(email, username)
# from auth_project.auth_project.settings import SECRET_KEY
# encoded_jwt = jwt.encode({'exp': 1657739340, 'iat': 1657739040, 'jti': '0507e460-78cb-4c83-aa2e-77c772b018fc', 'iss': 'https://id.pixomnia.com/realms/default'}, SECRET_KEY, algorithm="HS256", headers={"kid": "230498151c214b788dd97f22b85410a5"})
# print(encoded_jwt)
# a = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTc3MzkzNDAsImlhdCI6MTY1NzczOTA0MCwianRpIjoiMDUwN2U0NjAtNzhjYi00YzgzLWFhMmUtNzdjNzcyYjAxOGZjIiwiaXNzIjoiaHR0cHM6Ly9pZC5waXhvbW5pYS5jb20vcmVhbG1zL2RlZmF1bHQifQ.5pliMDBvC2F_O1BHYtQdtB7JBLCtuDRTjN-gC0rSoMQ'
# decoded_jwt = jwt.decode(a, options={"verify_signature": False})
# print(decoded_jwt)
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5FRTFRVVJCT1RNNE16STVSa0ZETlRZeE9UVTFNRGcyT0Rnd1EwVXpNVGsxUWpZeVJrUkZRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi04N2V2eDlydS5hdXRoMC5jb20vIiwic3ViIjoiYVc0Q2NhNzl4UmVMV1V6MGFFMkg2a0QwTzNjWEJWdENAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZXhwZW5zZXMtYXBpIiwiaWF0IjoxNTcyMDA2OTU0LCJleHAiOjE1NzIwMDY5NjQsImF6cCI6ImFXNENjYTc5eFJlTFdVejBhRTJINmtEME8zY1hCVnRDIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.PUxE7xn52aTCohGiWoSdMBZGiYAHwE5FYie0Y1qUT68IHSTXwXVd6hn02HTah6epvHHVKA2FqcFZ4GGv5VTHEvYpeggiiZMgbxFrmTEY0csL6VNkX1eaJGcuehwQCRBKRLL3zKmA5IKGy5GeUnIbpPHLHDxr-GXvgFzsdsyWlVQvPX2xjeaQ217r2PtxDeqjlf66UYl6oY6AqNS8DH3iryCvIfCcybRZkc_hdy-6ZMoKT6Piijvk_aXdm7-QQqKJFHLuEqrVSOuBqqiNfVrG27QzAPuPOxvfXTVLXL2jek5meH6n-VWgrBdoMFH93QEszEDowDAEhQPHVs0xj7SIzA"
# token_jwt = jwt.decode(token, options={"verify_signature": False})
# print(token_jwt)
# new_request = {}
# a = ['email', 'given_name', 'sid']
# for k, v in decoded.items():
#     if k in [i for i in a]:
#             if k == 'given_name':
#                 print(k)
#                 new_request['username'] = new_request.get('username', v)
#             else:
#                     new_request[k] = new_request.get(k, v)
# print(new_request)

# class PageNumberSetPagination(pagination.PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     ordering = 'date_added_post_db'
#
#
# class NewView(APIView):
#     pagination_class = PageNumberSetPagination
#
#     def get(self, request):
#
#         link = f'https://tlgrm.ru/channels/@showtimeinfo'
#         browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         browser.get(link)
#         time.sleep(1)
#         for i in range(2):
#             botton_next = browser.find_element(By.CLASS_NAME, "cfeed-loadmore-tear__button")
#             browser.execute_script("return arguments[0].scrollIntoView(true);", botton_next)
#             botton_next.click()
#             time.sleep(1)
#         time_create_post = browser.find_elements(By.XPATH, '//div[@channel_id="1143557060"]/header/section/footer/time')
#         title_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text > b")
#         dick_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text")
#         print(len(time_create_post), len(title_post), len(dick_post))
#         for i in range(len(time_create_post)):
#             time_cr = time_create_post[i].text
#             # print(i, '---------', time_create_post[i].text, title_post[i].text, dick_post[i].text)
#             old_create_time = ''
#             for k, v in data_time.items():
#                 if k == time_cr:
#                     old_create_time = datetime.now() - timedelta(minutes=v)
#             om = title_post[i].text
#             di_post = dick_post[i].text
#             di_post = (di_post.split('\n\n'))[1:-1]
#             di_post1 = ''.join(di_post)
#             check = New.objects.filter(name_public=om)
#             if not check:
#                 New.objects.create(name_public=om, information_post=di_post1, date_create_post=old_create_time)
#         all_news = New.objects.all()
#         serializer = NewSerializer(all_news, many=True)
#         return Response({'news': serializer.data})
# import time
# import datetime
# from datetime import datetime, timedelta
# a = '56 минут назад'
# if 'мин' in a:
#     min = int(a.split()[0])
#     old_create_time = datetime.now() - timedelta(minutes=min)
#     print(old_create_time)
# import time
# import schedule
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# options = Options()
# # options.add_argument("--headless")
# # options.add_argument("--disable-dev-shm-usage")
# # options.add_argument("--no-sandbox")
# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# import pandas as pd
# data = []
# for i in range(1, 3):
#     print(i)
#
#     url = f'https://kinogo.cx/filmy-2022/page/{i}/'
#     r = requests.get(url)
#     sleep(3)
#     soup = BeautifulSoup(r.text, 'lxml')
#     list_movies = soup.findAll('article', class_='short')
#     print(list_movies)

#     for i in list_movies:
#         name_movie = i.find('h2').find('a').text.split()[0]
#         article_movie = i.find('div', class_='kukuruk-text').find('div', class_='kukret-desc').text
#         year_create = i.findAll('div', class_='kukret-line')[1].text
#         city = i.findAll('div', class_='kukret-line')[2].text
#         time = i.findAll('div', class_='kukret-line')[5].text
#         data.append([name_movie, article_movie, year_create, city, time])
# print(data)
# header = ['name_movie', 'article_movie', 'year_create', 'city', 'time']
# # name_movie = soup.find('div', class_='short').find('div', class_='kukuruk-top fx-row').text
# # print(name_movie)
# df = pd.DataFrame(data, columns=header)
# df.to_excel('doc.xlsx')


# App api_id: 12172771
# App api_hash: b93303a5481a699022ba24ef16063a2a
# App title: parser_bot
# Short name: parserb
# Available MTProto servers
# Test configuration: 149.154.167.40:443
# Public keys:
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigvO/vBfqACJLZtS7QMgCGXJ6XIR
# yy7mx66W0/sOFa7/1mAZtEoIokDP3ShoqF4fVNb6XeqgQfaUHd8wJpDWHcR2OFwv
# plUUI1PLTktZ9uW2WE23b+ixNwJjJGwBDJPQEQFBE+vfmH0JP503wr5INS1poWg/
# j25sIWeYPHYeOrFp/eXaqhISP6G+q2IeTaWTXpwZj4LzXq5YOpk4bYEQ6mvRq7D1
# aHWfYmlEGepfaYR8Q0YqvvhYtMte3ITnuSJs171+GDqpdKcSwHnd6FudwGO4pcCO
# j4WcDuXc2CTHgH8gFTNhp/Y8/SpDOhvn9QIDAQAB
# -----END RSA PUBLIC KEY-----
# Production configuration: 149.154.167.50:443
# Public keys:
#
# -----BEGIN RSA PUBLIC KEY-----
# MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g
# 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO
# 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/
# +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9
# t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs
# 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB
# -----END RSA PUBLIC KEY-----

# import configparser
# import json
# from links import list_links
#
# from telethon.sync import TelegramClient
# from telethon import connection, utils
#
# # для корректного переноса времени сообщений в json
# from datetime import date, datetime
#
# # классы для работы с каналами
# from telethon.tl.functions.channels import GetParticipantsRequest
# from telethon.tl.types import ChannelParticipantsSearch
#
# # класс для работы с сообщениями
# from telethon.tl.functions.messages import GetHistoryRequest
#
# # Считываем учетные данные
# config = configparser.ConfigParser()
# config.read("config.ini")
#
# # Присваиваем значения внутренним переменным
# api_id = config['Telegram']['api_id']
# api_hash = config['Telegram']['api_hash']
# username = config['Telegram']['username']
# phone = '+375291811455'
#
# # Создадим объект клиента Telegram API:
# client = TelegramClient(username, api_id, api_hash)
#
# client.start()
#
#
# # async def dump_all_participants(channel):
# #   """Записывает json-файл с информацией о всех участниках канала/чата"""
# #   offset_user = 0    # номер участника, с которого начинается считывание
# #   limit_user = 20  # максимальное число записей, передаваемых за один раз
# #
# #   all_participants = []   # список всех участников канала
# #   filter_user = ChannelParticipantsSearch('')
# #
# #   while True:
# #     participants = await client(GetParticipantsRequest(channel,
# #       filter_user, offset_user, limit_user, hash=0))
# #     if not participants.users:
# #       break
# #     all_participants.extend(participants.users)
# #     offset_user += len(participants.users)
# #
# #   all_users_details = []   # список словарей с интересующими параметрами участников канала
# #
# #   for participant in all_participants:
# #     all_users_details.append({"id": participant.id,
# #       "first_name": participant.first_name,
# #       "last_name": participant.last_name,
# #       "user": participant.username,
# #       "phone": participant.phone,
# #       "is_bot": participant.bot})
# #
# #   for i in all_users_details:
# #     print(i)
# # print(f'**********************\n', i['message'], f'\n\n')
# #
# #   # with open('channel_users.json', 'w', encoding='utf8') as outfile:
# #   #   json.dump(all_users_details, outfile, ensure_ascii=False)
#
#
# async def dump_all_messages(channel, limit_msg):
#     """Записывает json-файл с информацией о всех сообщениях канала/чата"""
#     offset_msg = 0  # номер записи, с которой начинается считывание
#     limit_msg = 4   # максимальное число записей, передаваемых за один раз
#
#     all_messages = []  # список всех сообщений
#     total_messages = 0
#     total_count_limit = limit_msg  # поменяйте это значение, если вам нужны не все сообщения
#
#     # class DateTimeEncoder(json.JSONEncoder):
#     #   '''Класс для сериализации записи дат в JSON'''
#     #   def default(self, o):
#     #     if isinstance(o, datetime):
#     #       return o.isoformat()
#     #     if isinstance(o, bytes):
#     #       return list(o)
#     #     return json.JSONEncoder.default(self, o)
#
#     while True:
#         history = await client(GetHistoryRequest(
#             peer=channel,
#             offset_id=offset_msg,
#             offset_date=None, add_offset=0,
#             limit=limit_msg, max_id=0, min_id=0,
#             hash=0))
#         if not history.messages:
#             break
#         messages = history.messages
#         for message in messages:
#             all_messages.append(message.to_dict())
#         offset_msg = messages[len(messages) - 1].id
#         total_messages = len(all_messages)
#         if total_count_limit != 0 and total_messages >= total_count_limit:
#             break
#
#     chat = await client.get_entity(message.chat_id)  # Получаем чат по ИД
#     a = {}
#     for i in range(len(all_messages)):
#         text = all_messages[i]['message'].split('\n')
#         a.setdefault(chat.username, []).append((i + 1, text))
#         print(chat.title, '--------------------------------')
#         # print(chat.username)  # Юзернейм чата
#         # print(i)
#         # print(f'**********************\n', i['message'], f'\n\n')
#     print(a)
#     # with open('channel_messages.json', 'w', encoding='utf8') as outfile:
#     #   json.dump(all_messages, outfile, ensure_ascii=False, cls=DateTimeEncoder)
#
#
# async def main(list_links):
#     for link in list_links:
#         url = link
#         print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nurl = ', url)
#         channel = await client.get_entity(url)
#         channel_id = await client.get_entity(channel.title)
#         print(channel_id.id)
#         print(channel_id.title)
#         print(channel_id.photo)
#
#         # await dump_all_participants(channel)
#         await dump_all_messages(channel, limit_msg=1)
#
#
# with client:
#     client.loop.run_until_complete(main(list_links))
# from datetime import datetime
# a =datetime.strptime('2022-07-05T14:48:00.000Z', '%Y-%m-%dT%H:%M:%S.%f%z')
# cactom =datetime.strptime('2022-07-27T19:03:42.064846Z', '%Y-%m-%dT%H:%M:%S.%f%z')
# now = datetime.now()
# print(a)
# print(now)
# print(cactom)

import math

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(zip(*[iter(l)] * 3)))
# a = [1,2,3]
# b = ['one', 'two', 'tree']
# print(list(zip(a,b)))

import re

a = 'когда я шел backenf, бекенд  frodo шли гулять, backend по Devops и девоп'
backend = r'b[a,e][c,s]k\w*en[f,d]|б[е,э]к\w*[е,э]д'
sear = re.findall(backend, a)
print(sear)

test = 'аааБББввв'
pars = r'[А-Я]\w*[А-Я]'
print(re.search(pars, test))

