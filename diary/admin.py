from django.contrib import admin

from .models import CustomUser, Diary  ###1 追加###
admin.site.register(Diary) ###2 追加###
# Register your models here.
