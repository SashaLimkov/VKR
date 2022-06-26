from django.test import TestCase

# Create your tests here.
from usersupport.models import TelegramUser, Doctor


class TestModels(TestCase):
    def setUp(self):
        self.tg_user = TelegramUser.objects.create(
            user_id=11111,
            name="user",
            phone="89991629654",
            email="test@mail.ru"
        )

    def test_create_new_user_with_old_number(self):
        TelegramUser.objects.create(
            user_id=11242343,
            name="user3",
            phone="89961629654",
            email="testt@mail.ru"
        )
        TelegramUser.objects.create(
            user_id=1122343,
            name="user3",
            phone="89961629654",
            email="teswt@mail.ru"
        )

    def test_create_new_user_with_old_email(self):
        TelegramUser.objects.create(
            user_id=11225343,
            name="user3",
            phone="89971629654",
            email="teste@mail.ru"
        )
        TelegramUser.objects.create(
            user_id=1122343,
            name="user3",
            phone="89981629654",
            email="teste@mail.ru"
        )

    def test_create_doctor_with_too_long_exp(self):
        Doctor.objects.create(
            user=self.tg_user,
            education="sda",
            experience="JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ"
                       "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
                       "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
                       "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
            photo_id="sad",
            profession="sd",
            calendar_id="234"
        )

    def test_get_count_doctors(self):
        Doctor.objects.create(
            user=self.tg_user,
            education="sda",
            experience="we",
            photo_id="sad",
            profession="sd",
            calendar_id="234"
        )
        self.assertTrue(1 == len(Doctor.objects.all()))
