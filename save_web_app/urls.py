from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signin', views.signin, name='signin'),
    path('forget',views.forget, name='forget'),
    path('texteditor', views.texteditor, name='texteditor')
]
