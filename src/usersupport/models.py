from django.db import models


# Create your models here.
class TimeBasedModel(models.Model):
    """
    Время создания или обновления записи в бд
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(auto_now=True)


class TelegramUser(TimeBasedModel):
    """
    Пользователь телеграма и его контактные данные
    """

    class Meta:
        verbose_name = "Телеграм Юзер"
        verbose_name_plural = "Телеграм Юзеры"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name="UserID")
    name = models.CharField(max_length=255, verbose_name="UserName")
    phone = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=255, unique=True)


class Client(TimeBasedModel):
    """
    Клиент|пользователь клиники, содержит антропараметрические данные конкретного пользователя телеграмма
    """

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Телеграм Юзер", unique=True
    )
    gender = models.CharField(max_length=3, verbose_name="Пол")
    height = models.IntegerField(verbose_name="Рост")
    weight = models.IntegerField(verbose_name="Вес")
    age = models.IntegerField(verbose_name="Возраст")
    ims = models.CharField(max_length=255, verbose_name="ИМС")
    prediction = models.CharField(max_length=5000, verbose_name="Предварительный диагноз", default="")
    additional = models.CharField(max_length=5000, verbose_name="Дополнительная информация", default="")


class RegWorker(TimeBasedModel):
    """Регистрационный работник с его каналом и чатом"""

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
    """Анкета доктора с информацией о нем и календарем"""

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
    calendar_id = models.CharField(max_length=500, verbose_name="ID Календаря")


class UserRequest(TimeBasedModel):
    """Записи пользователей с информацией о них"""

    class Meta:
        verbose_name = "Запись пользователя"
        verbose_name_plural = "Записи пользователей"

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="Клиент"
    )
    file_name = models.CharField(
        max_length=200,
        unique=True, verbose_name="Файл"
    )
    date = models.CharField(
        max_length=100,
        verbose_name="Дата"
    )
    time = models.CharField(
        max_length=100,
        verbose_name="Время"
    )
    doc_id = models.IntegerField(
        verbose_name="ID Врача"
    )
