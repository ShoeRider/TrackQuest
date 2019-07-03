from django.urls import path
from . import views
from django.conf.urls import include, url


urlpatterns = [
    #path(r'Display/<slug:groupname>/', views.view_group,name='view-group'),
    #path(r'Edit/<slug:groupname>/', views.Edit_group,name='Edit_Group'),

    #path(r'Display/<slug:groupname>/Manage_Recruits/<slug:operation>/<int:userPK>', views.Manage_Recruits, name="Manage_Recruits"),
    #path(r'Display/<slug:groupname>/Manage_Members/', views.Manage_Members, name="Manage_Members"),
    #path(r'Display/<slug:groupname>/Manage_Privlege/<slug:operation>/<int:User_pk>', views.Manage_Privlege, name="Manage_Privlege"),

    path('create/', views.CreateGroup, name='create_group'),
    path('delete/<int:pk>/', views.GroupDelete.as_view(), name='delete_group'),


    #path(r'search/', views.searchGroup_Form,name='search_group'),
    #path(r'search/Results/', views.searchGroup_Results),


    #path(r'AllGroups/', views.list_groups, name="AllGroups"),

    #path(r'search/', views.searchGroup_Form,name='search_Groups'),
    #path(r'search/Results/', views.searchGroup_Results),

    #path(r'MyGroups/', views.List_UsersGroups, name="MyGroups"),


]
