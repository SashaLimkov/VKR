# Generated by Django 4.0.4 on 2022-05-24 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersupport', '0002_alter_client_ims'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersupport.telegramuser', unique=True, verbose_name='Телеграм Юзер'),
        ),
    ]