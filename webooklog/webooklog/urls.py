"""webooklog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from webooklog import views
from booklog import views as booklog_views

urlpatterns = [
    url(r'^$', booklog_views.index, name='index'),
    url(r'^booklog/', include('booklog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^accounts/login/$', views.login, name='account_login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change_done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset_done/(?P<url>.*)/$', views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<pk>.*)/(?P<token>.*)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset_complete/$', views.password_reset_complete, name='password_reset_complete'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
]
