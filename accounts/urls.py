from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'signup/', views.signup, name='signup'),
    url(r'', views.login, name='login'),
    url(r'logout/', views.logout, name='logout'),
    url(r'/(?P<username>[\w.@+-]+)/choose/', views.choose, name='choose'),
]