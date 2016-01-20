from django.conf.urls import url

from . import views

app_name = 'booklog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'detail/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/(?P<name>.*)/$', views.add, name='add'),
    url(r'^change/(?P<pk>[0-9]*)/$', views.change, name='change'),
    #url(r'detail/^(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>[0-9]+)/delete$', views.DetailView.as_view(), name='delete'),
    #url(r'^add$', views.DetailView.as_view(), name='add'),
]
