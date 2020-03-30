from django.urls import path
# from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # path('', csrf_exempt(views.ListProject.as_view())),
    # path('project', views.ListProject.as_view()),
    # path('student', views.ListStudent.as_view()),
    path('', views.index, name='index'),
    path('user', views.ListUser.as_view()),
    path('build', views.ListBuild.as_view()),
    path('skill', views.ListSkill.as_view()),
    path('item', views.ListItem.as_view()),
    path('buildgems', views.ListBuildGems.as_view()),
    path('buildcubes', views.ListBuildCubes.as_view()),
    path('builditems', views.ListBuildItems.as_view()),
    path('buildskills', views.ListBuildSkills.as_view()),
    path('votebuilduser', views.ListVoteBuildUser.as_view()),
    # path('<int:pk>/', csrf_exempt(views.DetailProject.as_view())),
    # path('<int:pk>/project', views.DetailProject.as_view()),
    # path('<int:pk>/student', views.DetailStudent.as_view()),
    path('<int:pk>/user', views.DetailUser.as_view()),
    path('<int:pk>/build', views.DetailBuild.as_view()),
    path('<int:pk>/skill', views.DetailSkill.as_view()),
    path('<int:pk>/item', views.DetailItem.as_view()),
    path('<int:pk>/buildgems', views.DetailBuildGems.as_view()),
    path('<int:pk>/buildcubes', views.DetailBuildCubes.as_view()),
    path('<int:pk>/builditems', views.DetailBuildItems.as_view()),
    path('<int:pk>/buildskills', views.DetailBuildSkills.as_view()),
    path('<int:pk>/votebuilduser', views.DetailVoteBuildUser.as_view()),
]
