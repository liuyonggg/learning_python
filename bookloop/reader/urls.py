from django.conf.urls import url
from reader import views

urlpatterns = [
    url(r'/book/recommend/(?P<pk>[0-9]+)/$', views.dummy_url_handler, name='recommand_book'),
    url(r'/book/finish/(?P<pk>[0-9]+)/$', views.dummy_url_handler, name='recommand_book'),
]
