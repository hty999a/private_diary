#####              #####
    #4つの追加or変更#
#####              #####
from django.urls import path ###1 追加###

from . import views ###2 追加###

app_name = "diary" ###3 追加###
urlpatterns = [  ###4 追加###
    path('', views.IndexView.as_view(), name="index")
]   ###4 追加###