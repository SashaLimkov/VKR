from django.db import models


# Create your models here.
class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_now=True)


class TelegramUser(TimeBasedModel):
    class Meta:
        verbose_name = "Телеграм Юзер"
        verbose_name_plural = "Телеграм Юзеры"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name="UserID")
    name = models.CharField(max_length=255, verbose_name="UserName")
    user_role = models.CharField(max_length=255, verbose_name="Роль", default="пользователь")
    phone = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=255, unique=True)


class Client(TimeBasedModel):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Телеграм Юзер"
    )
    height = models.IntegerField(verbose_name="Рост")
    weight = models.IntegerField(verbose_name="Вес")
    ims = models.IntegerField(verbose_name="ИМС")
    prediction = models.CharField(max_length=5000, verbose_name="Предварительный диагноз")
    additional = models.CharField(max_length=5000, verbose_name="Дополнительная информация")


class RegWorker(TimeBasedModel):
    class Meta:
        verbose_name = "Регистрационный работник"
        verbose_name_plural = "Регистрационные работники"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Телеграм Юзер"
    )
    chanel_id = models.BigIntegerField(verbose_name="Канал пользователя", default=0)
    chanel_chat_id = models.BigIntegerField(verbose_name="Чат пользователя", default=0)


class Doctor(TimeBasedModel):
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Телеграм Юзер"
    )
    education = models.CharField(max_length=5000, verbose_name="Образование")
    experience = models.CharField(max_length=255, verbose_name="Стаж")
    profession = models.CharField(max_length=255, verbose_name="Должность")
    photo_id = models.CharField(max_length=500, verbose_name="ID фото в телеграмм")


class UserQuestion(TimeBasedModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Телеграм Юзер"
    )
    question = models.CharField(max_length=5000, verbose_name="Анкета")
    state = models.CharField(
        max_length=100, verbose_name="Состояние", default="Открытая заявка"
    )
    mes_id = models.CharField(max_length=20000, unique=False, default="")
