from django.urls import path
from . import views
urlpatterns=[
    path('<int:id>/',views.emp_details,name='emp_details'),
    path('emp2/',views.emp2,name='emp2')
]