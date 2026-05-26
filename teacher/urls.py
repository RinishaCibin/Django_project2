from django.urls import path
from teacher.views import *

urlpatterns=[
    path('list',studentlistview.as_view(),name="slist"),
    path('add',AddStudentView.as_view(),name="sadd"),
    path('edit/<int:sid>',EditStudentView.as_view(),name="sedit"),
    path('delete/<int:sid>',DeleteStudentView.as_view(),name="stdelete"),
    path('hwlist',HomeWorklistView.as_view(),name="hwlist"),
    path('addhw',AddHomeworkView.as_view(),name='addhw'),
    path('deletehw/<int:hid>',DeleteHwView.as_view(),name='deletehw'),
    path('edithw/<int:hid>',EditHwView.as_view(),name="edithw")


]