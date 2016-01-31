"""bookloop URL Configuration

The `urlpatterns` list routes URLs to site. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function site
    1. Add an import:  from my_app import site
    2. Add a URL to urlpatterns:  url(r'^$', site.home, name='home')
Class-based site
    1. Add an import:  from other_app.site import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import View
from bookloop import sites
from reader.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^account/(?P<pk>[0-9]+)/$', sites.site.account, name='account'),
    url(r'^signup/$', sites.site.signup, name='signup'),
    url(r'^login/$', sites.site.login, name='login'),
    url(r'^logout/$', sites.site.logout, name='logout'),
    url(r'^password_change/$', sites.site.password_change, name='password_change'),
    url(r'^password_change/done/$', sites.site.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', sites.site.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', sites.site.password_reset_done, name='password_reset_done'),
    url(r'^password_reset/complete/$', sites.site.password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        sites.site.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reader/', include('reader.urls')),
    url(r'^admin/', admin.site.urls),
]
