from django.contrib import admin
from django.urls import path, include, re_path
from . import frontendViews
from . import views


urlpatterns = [
    # frontend starts
    re_path(r'^$', frontendViews.index, name='frontendindex'),
    re_path(r'^project/$', frontendViews.project, name='frontendproject'),
    # frontend ends
    re_path(r'^login/$', views.loginToDashboard, name='login'),
    re_path(r'^logout/$', views.logoutFromDashboard, name='logout'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^dashboard/$', views.home, name='home'),
    re_path(r'^home/page/setting/$', views.home_page, name='home_page'),
    re_path(r'^edit/home/page/setting/(?P<pk>\d+)/$', views.editHomePageInfo, name='editHomePageInfo'),
    re_path(r'^remove/home/page/setting/(?P<pk>\d+)/$', views.removeHomePageInfo, name='removeHomePageInfo'),
]
