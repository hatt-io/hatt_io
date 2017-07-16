from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
    url(r'^thinkings/$', views.thinkings, name='thinkings'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
urlpatterns += staticfiles_urlpatterns()
