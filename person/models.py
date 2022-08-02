from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager
from django.contrib.postgres.fields import ArrayField


class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


# 60 Получение связанных объектов. Related objects.
# https://www.youtube.com/watch?v=7mleEvxHpm0&list=PLQAt0m1f9OHvGM7Y7jAQP8TKbBd3up4K2&index=62
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=False, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(max_length=15, unique=True, null=True, blank=False)
    sub_phone = ArrayField(PhoneNumberField(max_length=15), unique=True, blank=True, null=True)
    explanation_by_phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=50, db_index=True, unique=True)
    sub_email = ArrayField(models.EmailField(max_length=50), unique=True, blank=True, null=True)
    explanation_by_email = models.CharField(max_length=30, blank=True, null=True)
    website = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    tags = TaggableManager(blank=True)
    event_birthday = ArrayField(models.CharField(max_length=80), blank=True, null=True)
    location = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    life_work = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    education = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    soc_network = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email


class TestPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.first_name


class NewPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    work_experience = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


def user_directory_path(instance, filename):
    return 'upload_file/user_{0}/{1}'.format(instance.first_name, filename)


class ContactsUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    notes = RichTextUploadingField(null=True, blank=True)
    education = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    website = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    upload_file = models.FileField(upload_to=user_directory_path, max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    iduserCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.first_name


class ContactsGF(models.Model):
    type = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True, null=True)
    id_email = models.CharField(max_length=200)
    idreator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_email


class ContactsGFNew(models.Model):
    type = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, blank=True, null=True)
    # id_email = models.CharField(max_length=200)
    idtor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.contact


class New(models.Model):
    title_post = models.CharField(max_length=250, blank=True, null=True)
    content_post = RichTextUploadingField(blank=True, null=True)
    date_create_post = models.DateTimeField(blank=True, null=True)
    date_added_post_db = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_post


class ContactFaceBook(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    created_contact = models.DateTimeField(auto_now_add=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class ContactGoogle1(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    created_contact = models.DateTimeField(auto_now_add=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class CalendarUser(models.Model):
    event = RichTextUploadingField()
    date_create_event = models.DateTimeField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event[:20]


class Event(models.Model):
    title_event = models.CharField(max_length=200)
    description = models.TextField()
    start_time_event_bd = models.DateTimeField()
    end_time_event = models.DateTimeField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_event
