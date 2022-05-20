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
    chanel_chat_id = models.BigIntegerField(verbose_name="Чат пользователя", default=0)
    chanel_id = models.BigIntegerField(verbose_name="Канал пользователя", default=0)


class UserQuestion(TimeBasedModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    question = models.CharField(max_length=5000, verbose_name="Анкета")
    state = models.CharField(
        max_length=100, verbose_name="Состояние", default="Открытый заявка"
    )
    mes_id = models.CharField(max_length=20000, unique=False, default="")

