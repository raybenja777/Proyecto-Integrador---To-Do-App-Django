# Generated by Django 5.0.3 on 2024-05-14 02:25

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('to_do_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('usuario_email', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('P', 'Pendiente'), ('C', 'Completado')], max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
