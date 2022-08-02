# Generated by Django 4.0.5 on 2022-08-02 17:45

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import person.models
import phonenumber_field.modelfields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=15, null=True, region=None, unique=True)),
                ('sub_phone', django.contrib.postgres.fields.ArrayField(base_field=phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None), blank=True, null=True, size=None, unique=True)),
                ('explanation_by_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True)),
                ('sub_email', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=50), blank=True, null=True, size=None, unique=True)),
                ('explanation_by_email', models.CharField(blank=True, max_length=30, null=True)),
                ('website', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('event_birthday', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=80), blank=True, null=True, size=None)),
                ('location', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('life_work', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('education', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('soc_network', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(blank=True, max_length=250, null=True)),
                ('content_post', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('date_create_post', models.DateTimeField(blank=True, null=True)),
                ('date_added_post_db', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('work_experience', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_event', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time_event_bd', models.DateTimeField()),
                ('end_time_event', models.DateTimeField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactsUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('notes', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('education', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('website', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None)),
                ('upload_file', models.FileField(blank=True, max_length=200, null=True, upload_to=person.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('iduserCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='ContactsGFNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('contact', models.CharField(blank=True, max_length=200, null=True)),
                ('idtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactsGF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('contact', models.CharField(blank=True, max_length=200, null=True)),
                ('id_email', models.CharField(max_length=200)),
                ('idreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactGoogle1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_contact', models.DateTimeField(auto_now_add=True)),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFaceBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_contact', models.DateTimeField(auto_now_add=True)),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CalendarUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_create_event', models.DateTimeField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('iduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
