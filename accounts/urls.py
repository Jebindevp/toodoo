from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('home/addtodo', views.add, name='addtodo'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]
