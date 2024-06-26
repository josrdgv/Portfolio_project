
from django.urls import path
from . import views


urlpatterns=[

    path('create/',views.user_reg,name='create'),
    path('register/',views.User_registration,name='register'),
    path('',views.login,name='login'),
    path('home/',views.User_home,name='home'),
    path('detail/<int:userid>',views.user_detail,name='detail'),
    path('update_profile/<int:userid>',views.update_profile,name='update_profile'),

]