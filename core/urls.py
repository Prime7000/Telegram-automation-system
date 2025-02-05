from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('home/',views.home, name='home'),
    path('',views.dashboard, name='dashboard'),
    path('bot_dashboard/',views.bot_dashboard, name='bot_dashboard'),
    path('add_bot/',views.add_bot, name='add_bot'),
    path('edit_task/<int:task_id>/',views.edit_task, name='edit_task'),
    path('edit_bot/<int:bot_id>/',views.edit_bot, name='edit_bot'),
    path('delete_task/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('delete_bot/<int:bot_id>/', views.delete_bot, name = 'delete_bot')

]