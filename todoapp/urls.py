from django.urls import path
from . import views

app_name = "todoapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add-task/', views.add_task, name='add_task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete_task'),
     path('edit-task/<int:id>/', views.edit_task, name='edit_task'),
]
