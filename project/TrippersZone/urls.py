from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django import forms
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^post/$', views.post),  # test post

    url(r'^login/$', views.login),
    url(r'^renter_login/$', views.renter_login),
    url(r'^renter_login/o_login/$', views.o_login),
    # url(r'^owner_login/login/renter_login'),
    url(r'^login/o_login/$', views.o_login),
    url(r'^signup/renter_login/$', views.renter_login),
    url(r'login/renter_login$', views.renter_login),
    url(r'login/index$', views.index),
    url(r'o_home/profile$', views.owner_profile),
    url(r'o_home/profile/create_post$', views.create_post),
    url(r'o_home/profile/logout$', views.index),
    url(r'^signup/$', views.signup),
    url(r'^renter_signup/$', views.renter_signup),
    url(r'^set_profile$', views.set_profile),
    url(r'^singupprocess', views.singupprocess),
    url(r'^owner_singupprocess', views.owner_singupprocess),
    url(r'^owner_signup', views.owner_signup),
    url(r'^owner_set_profile/owner_singupprocess', views.owner_singupprocess),
    url(r'o_home/profile/index$', views.index),
    url(r'signup/login$', views.login),

    url(r'^profile/$', views.profile),
    url(r'^profile/logout/$', views.logout),
    url(r'^owner_profile/o_list/$', views.o_list),
    url(r'^profile/r_list/$', views.o_list),
    url(r'^profile/ownerPostList/$', views.ownerPostList),
    url(r'^owner_profile/logout/$', views.logout),
    url(r'^profile/logout/$', views.logout),
    url(r'^renter_login/login$', views.login),

    url(r'^owner_profile/o_list/(.*)/$', views.test1),

    url(r'^o_home/$', views.o_home),
    url(r'^owner_profile/$', views.owner_profile),
    # url(r'^owner_profile/o_list/$', views.o_list),
    url(r'^profile/(.*)/$', views.test1),
    url(r'^createPost/$', views.create_post),
    url(r'^owner_profile/logout/$', views.logout),
    url(r'^owner_profile/create_post/$', views.create_post),
    url(r'^owner_profile/create_post/createPostProcess', views.createPostProcess),
    url(r'^owner_set_profile/$', views.owner_set_profile),

    url(r'^auth/', include('social_django.urls', namespace='social')),

]
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_URL_NAMESPACE = 'users:social'
