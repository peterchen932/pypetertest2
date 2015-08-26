from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
