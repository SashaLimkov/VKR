from django.contrib import admin

from ..models import TelegramUser, Client, RegWorker, Doctor, UserRequest


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "name",
        "phone",
        "email",
        "created_at",
        "updated_at",
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "height",
        "weight",
        "prediction",
        "additional",
        "created_at",
        "updated_at",
    )


class RegWorkerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "chanel_id",
        "chanel_chat_id",
    )


class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "education",
        "experience",
        "profession",
        "photo_id",
        "calendar_id"
    )


class URequestAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "file_name",
        "date",
        "time",
        "doc_id",
    )


# Register your models here.
admin.site.register(TelegramUser, UsersAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(RegWorker, RegWorkerAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(UserRequest, URequestAdmin)
