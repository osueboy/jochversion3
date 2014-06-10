from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'parcial.views.form_empleado', name='checkin'),
                       url(r'^checkin/$', 'parcial.views.landing', name='checkin'),
                       url(r'^admin/', include(admin.site.urls))
                       )
