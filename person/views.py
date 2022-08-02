import string
import time
import datetime
from datetime import datetime, timedelta
import random
from rest_framework.decorators import action

import schedule
from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse
from django.views import generic
import jwt
from rest_framework import viewsets, generics, permissions, status, filters, pagination
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from taggit.models import Tag
import psycopg2
from psycopg2 import OperationalError
from django.db.models import Q

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .parser import data_time, news_pars

User = get_user_model()
options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")

from .serializers import NewPersonHeroSerializer, RegisterSerializer, UserSerializer, ContactsUserSerializer, \
    TestPersonSerializer, ContactsGoogleFacebookSerializer, ContactsGoogleFacebookSerializerNew, \
    NewsSerializer, NewsLoaderSerializer, GiveNewTokenUserFaceBookSerializers, ContactFaceBookSerializers, \
    ContactGoogleSerializers, CalendarUserSerializers, CalendarUserEventSerializers

from .models import NewPerson, ContactsUser, ContactsGF, ContactsGFNew, New, ContactFaceBook, \
    CalendarUser, ContactGoogle1, Event

li_seria = ["NewPersonHeroSerializer", "RegisterSerializer", "UserSerializer", "ContactsUserSerializer"]


class NewQueryView(APIView):

    def post(self, request):
        dic_user = request.data  # получаем запрос в виде словаря
        name_class = ''
        for k, v in dic_user.items():  # проходим по словарю и достаем название таблицы
            if k == 'type' and v in li_seria:
                name_class = v
        # ищем созданную модель в models.py,
        # если есть сериализуем и добавляем в созданную таблицу
        if name_class:
            type_serial = eval(name_class)  # приводим строку к классу и подставляем в сериализатор
            serializer = type_serial(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'User created',
                             'user': serializer.data})
        else:  # если нет в models  моделей, подключаемся к БД напрямую
            name_field = {}
            name_table = ''
            name_field_for_found = []
            list_fields_names = []
            for key, val in dic_user.items():
                if key == 'type':
                    name_table = val
                else:
                    if key != 'type':
                        # name_field[key] = name_field.get(key,'VARCHAR(100) UNIQUE')  # формируем и добавляем уникальные поля
                        name_field[key] = name_field.get(key, 'VARCHAR(100)')  # формируем и добавляем уникальные поля
                        name_field_for_found.append(key)
                        list_fields_names.append(val)  # формируем и добавляем значения ключа
            list_fields_names = tuple(list_fields_names)  # переводим в картеж для отправки в БД
            name_field['date'] = 'timestamp DEFAULT NOW()'
            now_time = datetime.datetime.now()
            list_fields_names = list_fields_names + (str(now_time),)

            def create_connection(db_name, db_user, db_password, db_host, db_port):  # подключаемся к БД
                connection = None
                try:
                    connection = psycopg2.connect(
                        database=db_name,
                        user=db_user,
                        password=db_password,
                        host=db_host,
                        port=db_port,
                    )
                    print('Connection to PosrgresQL DB successfull')
                except OperationalError as e:
                    print(f"The error '{e}' occurred")
                return connection

            con = create_connection("DB1", "postgres", "root", "127.0.0.1", "5432")

            # con = create_connection("dc81ggqrnpkve6", "qkaxzsjgiqguhb",
            #                         "8192f49013a9aa4af326f7b1bb58c32ba4afec96bb149e5e07cbef072591a47e",
            #                         "ec2-18-204-142-254.compute-1.amazonaws.com", "5432")

            def check_name_db(connection):
                cursor = connection.cursor()
                # connection.autocommit = True
                # отправляем запрос в БД на получение всех таблиц
                cursor.execute(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog')")
                find_name_inbd = ''
                for x in cursor:
                    if name_table in x:  # ищем таблицу в БД, если есть добавляем в find_name_inbd, если нет создаем новую
                        find_name_inbd = name_table
                print(f" DB {find_name_inbd} exists")
                if find_name_inbd:  # если таблица есть в БД, добавляем значения
                    try:
                        users = list_fields_names
                        result_field_update = ', '.join(f'{keys}' for keys, value in name_field.items())
                        user_records = ", ".join(["%s"] * len(users))
                        insert_query = (
                            f"INSERT INTO {name_table} ({result_field_update}) VALUES ({user_records})"
                        )
                        cursor.execute(insert_query, users)
                        connection.commit()
                        name_field_for_found_d = ', '.join(name_field_for_found)
                        insert_query_del = (f" DELETE FROM {name_table} WHERE id IN (SELECT id FROM"
                                            f" (SELECT id, ROW_NUMBER() OVER ("
                                            f" PARTITION BY {name_field_for_found_d} ORDER BY  id DESC)"
                                            f" AS rn FROM {name_table}) t"
                                            f" WHERE t.rn > 1)")

                        cursor.execute(insert_query_del)
                        connection.commit()
                        return Response({'message': 'Informations added'})
                    except OperationalError as e:
                        print(f"The error '{e}' occurred")
                else:  # если таблицы в БД нет, создаем новую и сразу запалняем ее значениями
                    try:
                        result_field = ', '.join(f'{keys} {value}' for keys, value in name_field.items())
                        query = f"CREATE TABLE IF NOT EXISTS {name_table} (id SERIAL PRIMARY KEY, {result_field})"
                        cursor.execute(query)
                        connection.commit()
                        users = list_fields_names
                        result_field_update = ', '.join(f'{keys}' for keys, value in name_field.items())
                        user_records = ", ".join(["%s"] * len(users))
                        insert_query = (
                            f"INSERT INTO {name_table} ({result_field_update}) VALUES ({user_records})"
                        )
                        cursor.execute(insert_query, users)
                        connection.commit()
                        return Response({'message': f' Table {name_table} created, informations added'})
                    except OperationalError as e:
                        print(f"The error '{e}' occurred")
                    finally:
                        if connection:
                            cursor.close()
                            connection.close()
                            return f"Соединение с PostgreSQL закрыто"

            check_name_db(con)
            return Response({'complete': f'Informations added'})


class DashboardUserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            return User.objects.filter(email=id_user)


class ContactsUsersView(viewsets.ModelViewSet):
    queryset = ContactsUser.objects.all()
    serializer_class = ContactsUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            print(id_user)
            return ContactsUser.objects.filter(iduserCreator=id_user)


class TagDetailView(generics.ListAPIView):
    serializer_class = ContactsUserSerializer
    permission_classes = [permissions.AllowAny]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            tag_slug = self.kwargs['tag_slug'].lower()
            tag = Tag.objects.get(slug=tag_slug)
            return ContactsUser.objects.filter(iduserCreator=id_user, tags=tag)


def main(request):
    return HttpResponse("It's work")


class NewPersonViewsets(viewsets.ModelViewSet):
    queryset = NewPerson.objects.all().order_by('first_name')
    serializer_class = NewPersonHeroSerializer

    lookup_field = 'first_name'


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user = serializer.save()
        return Response({
            # "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
            'data': serializer.data
        })


class AllUsersViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersView(APIView):
    def get(self, request):
        w = User.objects.all()
        serializer = UserSerializer(w, many=True)
        return Response({'user': serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # new_user = User.objects.create(
        #     username=request.data['username'],
        #     password=request.data['password']
        # )
        # return Response({'message': 'User created',
        #                  'user': UserSerializer(new_user).data})
        print(serializer.data)
        return Response({'message': 'User created',
                         'user': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'insert key'})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({'error': 'not created'})

        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user update': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(pk=pk).delete()
        return Response({'data': str(user)})


class FindUser(APIView):
    def get(self, request):
        users = NewPerson.objects.all()
        return Response({'user': NewPersonHeroSerializer(users, many=True).data})


class FindUserOne(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response({'data': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(pk=pk).delete()
        return Response({'data': str(user)})


class UserApiViewList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateList(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserOne(APIView):

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Bad request'})
        inst = User.objects.get(pk=pk)
        serializer = UserSerializer(data=request.data, instance=inst)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ContactsGoogleFacebook(viewsets.ModelViewSet):  # GET, POST,
    queryset = ContactsGF.objects.all()
    serializer_class = ContactsGoogleFacebookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            print(id_user)
            return ContactsGF.objects.filter(idreator=id_user)

    # def get(self, request):
    #     queryset = ContactsGF.objects.all()
    #     serializer = ContactsGoogleFacebookSerializer(queryset, many=True)
    #     return Response({'all contacts': serializer.data})

    def post(self, request):
        print('REQUEST= ', request)
        serializer = ContactsGoogleFacebookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        print('serializer.data = ', serializer.data)

        if serializer.data.get('id_email') == 'this field exists':
            return Response({'error': 'This contact exists already'})
        else:
            print('serializer.data1= ', serializer.data)
            return Response({'data': serializer.data})


class ContactsGoogleFacebookNew(APIView):  # GET, POST,
    serializer_class = ContactsGoogleFacebookSerializerNew
    permission_classes = [permissions.AllowAny]

    # def get_queryset(self):
    #     if IsAuthenticated:
    #         id_user = User.objects.get(id=self.request.user.id)
    #         print(id_user)
    #         return ContactsGF.objects.filter(idreator=id_user)

    # def get(self, request):
    #     queryset = ContactsGFNew.objects.all()
    #     serializer = ContactsGoogleFacebookSerializerNew(queryset, many=True)
    #     return Response({'all contacts': serializer.data})

    def post(self, request):
        serializer = ContactsGoogleFacebookSerializerNew(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_email = request.data['id_email']
        contact = request.data['contact']
        type = request.data['type']
        email_exist = User.objects.filter(email=id_email)
        if email_exist:
            id_user = User.objects.values('id').get(email=id_email)['id']  # list(email_exist.values_list('id'))[0][0]
            check_cont = ContactsGFNew.objects.values_list('contact').filter(
                idtor_id=id_user,
                type=type
            )
            for i in check_cont:
                if contact in i:
                    return Response({'message': 'Contact exist already'})

            # если такой контакт не найден, а user существует в базе user'ов
            else:
                new_post = ContactsGFNew.objects.create(
                    idtor_id=id_user,
                    # id_email = id_email,
                    contact=contact,
                    type=type
                )
                serializer = ContactsGoogleFacebookSerializerNew(new_post)
                return Response({'new post': serializer.data})
        else:
            return Response({'message': f'user {id_email} does not exist'})


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = 'date_added_post_db'


class NewLoaderView(APIView):
    pagination_class = PageNumberSetPagination

    def get(self, request):

        # link = f'https://tlgrm.ru/channels/@showtimeinfo'
        # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # browser.get(link)
        # time.sleep(1)
        # for i in range(4):
        #     botton_next = browser.find_element(By.CLASS_NAME, "cfeed-loadmore-tear__button")
        #     browser.execute_script("return arguments[0].scrollIntoView(true);", botton_next)
        #     botton_next.click()
        #     time.sleep(1)
        # time_create_post = browser.find_elements(By.XPATH, '//div[@channel_id="1143557060"]/header/section/footer/time')
        # title_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text > b")
        # dick_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text")
        # def news_pars():
        #     link = f'https://tlgrm.ru/channels/@showtimeinfo'
        #     browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #     browser.get(link)
        #     time.sleep(1)
        #     # for i in range(2):
        #     #     botton_next = browser.find_element(By.CLASS_NAME, "cfeed-loadmore-tear__button")
        #     #     browser.execute_script("return arguments[0].scrollIntoView(true);", botton_next)
        #     #     botton_next.click()
        #     #     time.sleep(1)
        #     time_create_post = browser.find_elements(By.XPATH,
        #                                              '//div[@channel_id="1143557060"]/header/section/footer/time')
        #     title_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text > b")
        #     dick_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text")
        #     return time_create_post, title_post, dick_post
        # test = news_pars()
        def repeat_pars():
            parser = news_pars()

            def create_post(time_create_post, title_post, dick_post):
                min_post = min(len(time_create_post), len(title_post), len(dick_post))

                for i in range(min_post):
                    time_cr = time_create_post[i].text
                    old_create_time = ''

                    for k, v in data_time.items():

                        if 'мин' in time_cr:
                            minute = int(time_cr.split()[0])
                            old_create_time = datetime.now() - timedelta(minutes=minute)
                        else:
                            if k == time_cr:
                                old_create_time = datetime.now() - timedelta(minutes=v)

                    t_post = title_post[i].text
                    cont_post = dick_post[i].text
                    cont_post = (cont_post.split('\n\n'))[1:-1]
                    cont_post1 = ''.join(cont_post)
                    check_post_in_db = New.objects.filter(title_post=t_post)
                    if not check_post_in_db:
                        New.objects.create(title_post=t_post, content_post=cont_post1, date_create_post=old_create_time)

            create_post(*parser)

        # schedule.every(2).hour.do(repeat_pars)
        schedule.every(55).minutes.do(repeat_pars)

        while True:
            schedule.run_pending()
            time.sleep(1)


class NewsAboutView(viewsets.ModelViewSet):  # GET, POST,
    queryset = New.objects.order_by('-id')
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]

    # user = User.objects.filter(email=id_email)  # проверка существует ли такой user

    # if user:
    #     id_queryset_user = User.objects.values('id').get(email=id_email)['id']  # id user'a по email
    #
    #     # получить все контакты у этого user'а по type из request'а
    #     contacts_list = ContactsGF.objects.filter(
    #         id_user_creator_id=id_queryset_user,
    #         type_contact=type_contact,
    #     ).values_list('contacts')
    #
    #     for i in contacts_list:  # проверка на совпадение contacts из request с существующими contacts
    #         if contacts in i:
    #             return Response({'message': 'contact exists already'})
    #
    #     new_post = ContactsGF.objects.create(
    #         id_user_creator_id=id_queryset_user,
    #         contacts=contacts,
    #         type_contact=type_contact
    #     )
    #     return Response({'new post': SetPullFromFrontendSerializer(new_post).data})
    #
    # else:
    #     return Response({'message': f'user {id_email} does not exist'})


def check_bd(request):
    find_person = NewPerson.objects.all()
    get_one = NewPerson.objects.get(id=2)
    link = f'https://tlgrm.ru/channels/@showtimeinfo'
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get(link)
    time.sleep(1)
    title_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text > b")
    for i in title_post:
        om = i.text
        New.objects.create(name_public=om)
    all_news = New.objects.all()
    return render(request, 'person/main.html', {'find_person': find_person, 'get_one': get_one, 'all_news': all_news})


class GetTokenFaceBook(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def getRandomNumKey(self):
        num = 9
        a = string.ascii_letters + string.digits  # Источник данных: a-z, A-Z, 0-9
        key = random.sample(a, num)
        keys = "".join(key)
        return keys

    def post(self, request):
        token = request.data['token']
        decoded = jwt.decode(token, options={"verify_signature": False})
        email = decoded['email']
        password = self.getRandomNumKey()
        new_user = {
            'email': email,
            'password': password
        }
        check_user_in_bd = User.objects.filter(email=email)
        if not check_user_in_bd:
            serializer = self.get_serializer(data=new_user)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Пользователь успешно создан",
                'data': serializer.data
            })
        else:
            user = User.objects.get(email=new_user['email'])
            serializer = GiveNewTokenUserFaceBookSerializers(user)
            return Response({
                "message": "User exist already",
                'data': serializer.data
            })


class ContactFaceBookViews(viewsets.ModelViewSet):
    queryset = ContactFaceBook.objects.all()
    serializer_class = ContactFaceBookSerializers
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            return ContactFaceBook.objects.filter(iduser=id_user)


class ContactGoogleViews(viewsets.ModelViewSet):
    queryset = ContactGoogle1.objects.all()
    serializer_class = ContactGoogleSerializers
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            return ContactGoogle1.objects.filter(iduser=id_user)


class CalendarUserViews(viewsets.ModelViewSet):
    queryset = CalendarUser.objects.all()
    serializer_class = CalendarUserSerializers
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            return CalendarUser.objects.filter(iduser=id_user)


class GetEventCalendarView(generics.GenericAPIView):
    serializer_class = CalendarUserSerializers
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            # id_queryset_user = User.objects.values('id').get(email=id_user)['id']
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            event = request.data['event']
            date_create_event = request.data['date_create_event']
            # print(id_queryset_user)
            if not date_create_event:
                find_event = CalendarUser.objects.filter(event__icontains=event, iduser=id_user)
                if find_event:
                    serializer = CalendarUserSerializers(find_event, many=True)
                    return Response({'answer': serializer.data})
            else:
                find_event = CalendarUser.objects.filter(
                    Q(event__icontains=event) | Q(date_create_event=date_create_event), iduser=id_user)
                if find_event:
                    serializer = CalendarUserSerializers(find_event, many=True)
                    return Response({'answer': serializer.data})
            return Response({'answer': 'Nothing found for your request'})

# Response({'user': NewPersonHeroSerializer(users, many=True).data}

class CalendarUserEventViews(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = CalendarUserEventSerializers
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if IsAuthenticated:
            id_user = User.objects.get(id=self.request.user.id)
            return CalendarUser.objects.filter(iduser=id_user)