from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('register/',views.register_page,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('add-task/',views.add_task,name='add-task'),
    path('edit-task/<int:id>/',views.edit_task,name='edit-task'),
    path('delete-task/<int:id>/',views.delete_task,name='delete-task'),
]