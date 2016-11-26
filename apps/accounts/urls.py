from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'AdminLTE/login.html'}),
    #url(r'^', include('django.contrib.auth.urls')),
]
