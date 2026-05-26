from django.urls import path
from office.views import *

urlpatterns=[
    path('',OfficeHomeView.as_view(),name="officehome")

]