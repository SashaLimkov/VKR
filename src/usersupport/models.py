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
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, verbose_name="UserID")
    name = models.CharField(max_length=255, verbose_name="UserName")
    user_role = models.CharField(max_length=255, verbose_name="Роль")
    state = models.IntegerField(verbose_name="Работает?", default=1)
    phone = models.CharField(max_length=12, unique=True)
    chat_id = models.BigIntegerField(verbose_name="Чат пользователя", default=0)
    chanel_id = models.BigIntegerField(verbose_name="Канал пользователя", default=0)

