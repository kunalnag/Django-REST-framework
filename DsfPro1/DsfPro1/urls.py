
from django.contrib import admin
from django.urls import path
from api1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/<int:pk>/', views.student_detail),
    path('studentinfo/', views.student_list),
    path('stucreate/', views.create),

]
