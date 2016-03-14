from django.conf.urls import url
from django.contrib import admin
from mysite.views import *
from books import views
from contact.views import contact, thanks


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks/$', thanks),
]
