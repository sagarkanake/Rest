from django.contrib import admin
from api import views
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    # url('studentapi/', views.StudentList.as_view()),
    # url('studentapi/', views.StudentCreate.as_view()),
    # url('studentapi/(?P<pk>\d+)/', views.StudentRetrieve.as_view()),
    # url('studentapi/(?P<pk>\d+)/', views.StudentUpdate.as_view()),
    # url('studentapi/(?P<pk>\d+)/', views.StudentDestroy.as_view()),
    url('studentapi/', views.StudentListCreate.as_view()),
    # url('studentapi/(?P<pk>\d+)/', views.RetrieveUpdateAPIView.as_view()),
    # url('studentapi/(?P<pk>\d+)/', views.StudentRetrieveDestroy.as_view()),
    url('studentapiGet/(?P<pk>\d+)/', views.StudentRetrieveUpdateDestroy.as_view()),
    
    
]