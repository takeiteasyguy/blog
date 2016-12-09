from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # AUTH
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),

    # REST
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),

]
