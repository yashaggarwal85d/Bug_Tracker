from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'projects'

urlpatterns = [
    url(r"^$", views.ListProjects, name="all"),
    url(r"^new/$", views.CreateProject.as_view(), name="create"),
    url(r"^issues/in/(?P<pk>\d+)/$",views.SingleProject.as_view(),name="single"),
    url(r"join/(?P<pk>\d+)/$",views.JoinProject.as_view(),name="join"),
    url(r"leave/(?P<pk>\d+)/$",views.LeaveProject.as_view(),name="leave"),
    url(r"delete/(?P<pk>\d+)/$",views.DeleteProject.as_view(),name="delete"),
    url(r"tagged/(?P<pk>\d+)/$",views.tagged,name="tagged"),
    url(r"complete/(?P<pk>\d+)/$",views.CompleteProject,name="complete"),
    url(r"joinper/(?P<pk>\d+)/$",views.CloseOrOpenJoin,name="joinper"),
    
    url(r"project_detail_api/(?P<pk>\d+)/$", views.project_detail_api, name="project_detail_api"),
    path('project_github_post/<str:pk>/<str:owner>/<str:repo>/',views.project_github_post, name="project_github_post"),
    url(r"projects_list_api/$", views.projects_list_api, name="projects_list_api"),
]