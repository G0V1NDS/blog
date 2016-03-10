from django.conf.urls import url

from app.blogApp import views

app_name='blogApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^delete/$',views.delete_comment,name='delete_comment'),
    # url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='post'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.comment, name='comment')
]
