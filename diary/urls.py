#####              #####
    #4つの追加or変更#
#####              #####
from django.urls import path ###1 追加###

from . import views ###2 追加###

# app_name = "diary" ###3 追加### ###これは同じアプリに同じリンクが二つ以上あるとき、使って、区別するらしい
urlpatterns = [  ###4 追加###
    path('', views.IndexView.as_view(), name='index'),
    path('member_ship/', views.Member_ShipView.as_view(), name='member_ship'),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    # path('inquiry/', views.InquiryView.as_view(), name='inquiry')
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'), ##関数ビューは()いらない
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
]   ###4 追加###


#これらはallauth.urlsに書いている(俺らには見えないけど。)。だから、かかなくていい
    # path('signup/', views.SignupView.as_view(), name='signup'),
    # path('login/', views.LoginView.as_view(), name='login'),