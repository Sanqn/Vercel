from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import NewPerson, ContactsUser, TestPerson, ContactsGF, ContactsGFNew, New, ContactFaceBook, \
    CalendarUser, ContactGoogle1, Event
from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from taggit.serializers import TagListSerializerField, TaggitSerializer


class ContactsUserSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    # iduserCreator = serializers.SlugRelatedField(slug_field="id", queryset=User.objects.all())
    iduserCreator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ContactsUser
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'photo', 'notes', 'iduserCreator', 'tags')
        # extra_kwargs = {"photo": {"read_only": True}}


class NewPersonHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPerson
        fields = ('id', 'first_name', 'last_name', 'email', 'work_experience')
        lookup_field = 'first_name'
        extra_kwargs = {
            'url': {'lookup_field': 'first_name'}
        }


class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        read_only_fields = ['username']
        fields = [
            # "username",
            "email",
            "password",
            # "password2",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        # username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        # password2 = validated_data["password2"]
        if not password:
            raise serializers.ValidationError({"password": "Введите пароль"})
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(TaggitSerializer, serializers.ModelSerializer):
    email = serializers.EmailField(required=True, trim_whitespace=True)
    tags = TagListSerializerField()

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'second_name',
                  'phone',
                  'sub_phone',
                  'explanation_by_phone',
                  'email',
                  'sub_email',
                  'explanation_by_email',
                  'website',
                  'tags',
                  'event_birthday',
                  'location',
                  'life_work',
                  'education',
                  'soc_network',
                  )
        # extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TestPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPerson
        fields = '__all__'


class ContactsGoogleFacebookSerializer(serializers.ModelSerializer):
    idreator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ContactsGF
        fields = '__all__'

    def create(self, validated_data):
        contact_type = validated_data.get('type')
        contact_id_email = validated_data.get('id_email')

        setorder = ContactsGF.objects.filter(type=contact_type, id_email=contact_id_email)
        print(setorder, '---------------------------------')
        if setorder:
            return {
                'type': 'this field exists',
                'id_email': 'this field exists',
                'contact': ''
            }
        else:
            return ContactsGF.objects.create(**validated_data)


class ContactsGoogleFacebookSerializerNew(serializers.ModelSerializer):
    # idtor = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ContactsGFNew
        fields = [
            # 'id_email',
            'contact',
            'type'
            # 'idtor'

        ]

    # def create(self, validated_data):
    #     return ContactsGFNew.objects.create(**validated_data)


class NewsLoaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'


# class WoomenModel:
#
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# class WoomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
#
# def encode():
#     model = WoomenModel('Gooroo', 'Hooroo')
#     model_st = WoomenSerializer(model)
#     print(model_st.data, type(model_st.data)) #{'title': 'Gooroo', 'content': 'Hooroo'}
#     render = JSONRenderer().render(model_st.data)
#     print(render) #b'{"title":"Gooroo","content":"Hooroo"}'
#
# def decode():
#     streem = io.BytesIO(b'{"title":"Gooroo","content":"Hooroo"}')
#     data = JSONParser().parse(streem)
#     print(data) # {'title': 'Gooroo', 'content': 'Hooroo'}
#     serializer = WoomenSerializer(data=data)
#     print(serializer) #WoomenSerializer(data={'title': 'Gooroo', 'content': 'Hooroo'}):
#                         # title = CharField(max_length=255)
#                         # content = CharField()
#     serializer.is_valid()
#     print(serializer.validated_data) # OrderedDict([('title', 'Gooroo'), ('content', 'Hooroo')])

class GiveNewTokenUserFaceBookSerializers(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "email",
            "token",
        ]

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class ContactFaceBookSerializers(serializers.ModelSerializer):
    iduser = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ContactFaceBook
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'iduser',
        ]


class ContactGoogleSerializers(serializers.ModelSerializer):
    iduser = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ContactGoogle1
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'iduser',
        ]


class CalendarUserSerializers(serializers.ModelSerializer):
    iduser = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CalendarUser
        fields = [
            'event',
            'date_create_event',
            'iduser'
        ]


class CalendarUserEventSerializers(serializers.ModelSerializer):
    id_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = [
            'title_event',
            'description',
            'start_time_event_bd',
            'end_time_event',
            'id_user'
        ]
