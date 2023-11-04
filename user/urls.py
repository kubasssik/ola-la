from django.urls import path
from user.views import login, registration, logout

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),#http://namesite/user/login/
    path('registration/', registration, name='registration'), 
    path('logout/', logout, name='logout'),  
]