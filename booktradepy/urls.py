from django.conf.urls import patterns, include, url

urlpatterns = url('change.views', 
        url('^$', 'listBook'),
        )
