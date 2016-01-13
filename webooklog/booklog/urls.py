from django.conf.urls import url

from . import views

app_name = 'booklog'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/delete$', views.DetailView.as_view(), name='delete'),
    #url(r'^add$', views.DetailView.as_view(), name='add'),
]
