# Generated by Django 4.0.4 on 2022-05-24 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersupport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ims',
            field=models.CharField(max_length=255, verbose_name='ИМС'),
        ),
    ]
