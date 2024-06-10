# Generated by Django 4.2.13 on 2024-06-08 07:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import services._shared.third_party.storage.azure
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guid', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('metadata', models.JSONField()),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('CANCELLED', 'Cancelled'), ('FAILED', 'Failed'), ('HIDDEN', 'Hidden'), ('INACTIVE', 'Inactive'), ('NEW', 'New'), ('PROCESSED', 'Processed'), ('SENT', 'Sent'), ('STARTED', 'Started'), ('SUCCESSFUL', 'Successful')], default='ACTIVE', max_length=32)),
                ('avatar', models.ImageField(blank=True, null=True, storage=services._shared.third_party.storage.azure.CustomAzureStorage(), upload_to='')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guid', models.CharField(default=uuid.uuid4, max_length=36, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('metadata', models.JSONField()),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('CANCELLED', 'Cancelled'), ('FAILED', 'Failed'), ('HIDDEN', 'Hidden'), ('INACTIVE', 'Inactive'), ('NEW', 'New'), ('PROCESSED', 'Processed'), ('SENT', 'Sent'), ('STARTED', 'Started'), ('SUCCESSFUL', 'Successful')], default='ACTIVE', max_length=32)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=24)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'apps',
            },
        ),
    ]