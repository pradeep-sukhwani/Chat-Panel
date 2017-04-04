from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^chat_panel/$', views.chat_panel, name='chat_panel'),

    url(r'^post/$', views.post, name='post'),
    url(r'^messages/$', views.messages, name='messages'),
]
