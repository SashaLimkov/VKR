# Generated by Django 4.0.4 on 2022-05-24 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersupport', '0003_alter_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersupport.telegramuser', unique=True, verbose_name='Телеграм Юзер'),
        ),
    ]
