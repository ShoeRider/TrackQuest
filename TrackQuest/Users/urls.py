from django.urls import path
from . import views
from django.conf.urls import include, url

# Setting up required urlpatterns
urlpatterns = [
    path('', views.View_Site_Dashboard,name='View_Site_Dashboard'),
    path('<slug:username>', views.view_user,name='View_User'),

    url(r'^EditProfile/(?P<pk>\d+)/$', views.EditProfile.as_view(), name='Edit_UserProfile'),
    path('LogIn/', views.LogIn,name="LogIn"),
    path('LogOut/', views.LogOut,name="LogOut"),
    #path('accounts/profile/', views.Profile, name='Profile'),
    path('SignUp/', views.SignUp.as_view(), name='SignUp'),
    path('Base/', views.Base, name='Base'),
    #path('', views.Base,name='Base'),
    #path('', views.MineYTData_Dashboard,name='MineYouTube'),
    #path('NavigateYouTube/', views.NavigateYouTube,name='NavigateYouTube'),
]
