from django.contrib import admin
from . import models


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass
# Register your models here.
