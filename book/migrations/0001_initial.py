# Generated by Django 4.1.7 on 2023-03-28 16:37

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, default='2000-10-01', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('FINANCE', 'FIN'), ('POLITICS', 'POL'), ('POWER', 'POW'), ('COMEDY', 'COM')], default='FIN', max_length=45)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('language', models.CharField(choices=[('ENGLISH', 'ENG'), ('HAUSA', 'HAU'), ('IGBO', 'IGB'), ('YORUBA', 'YOR')], default='YOR', max_length=45)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='book.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('REQUESTED', 'Requested'), ('ISSUED', 'Issued'), ('RETURNED', 'Returned'), ('OVERDUE', 'Overdue'), ('CANCELLED', 'Cancelled')], default='Available', max_length=45)),
                ('imprint', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.book')),
                ('borrower', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
