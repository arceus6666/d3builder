from django.urls import path

from . import views

_index = [path('', views.index, name='index')]

_all = [
    path('user', views.ListUser.as_view()),
    path('build', views.ListBuild.as_view()),
    path('skill', views.ListSkill.as_view()),
    path('item', views.ListItem.as_view()),
    path('buildgems', views.ListBuildGems.as_view()),
    path('buildcubes', views.ListBuildCubes.as_view()),
    path('builditems', views.ListBuildItems.as_view()),
    path('buildskills', views.ListBuildSkills.as_view()),
    path('votebuilduser', views.ListVoteBuildUser.as_view()),
]

_byid = [
    path('user/<str:uid>', views.userbyid, name='getbyid'),
    path('build/<str:bid>', views.buildbyid, name='getbyid'),
    path('skill/<str:sid>', views.skillbyid, name='getbyid'),
    path('item/<str:iid>', views.itembyid, name='getbyid'),
    path('buildgems/<str:bgid>', views.buildgemsbyid, name='getbyid'),
    path('buildcubes/<str:bcid>', views.buildcubesbyid, name='getbyid'),
    path('builditems/<str:biid>', views.builditemsbyid, name='getbyid'),
    path('buildskills/<str:bsid>', views.buildskillsbyid, name='getbyid'),
    path('votebuilduser/<str:vbuid>', views.votebuiluserdbyid, name='getbyid'),
]

urlpatterns = _index + _all + _byid
