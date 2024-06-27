from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    path('create/', views.TodoCreate.as_view(), name='create'),
    path('', views.TodoList.as_view(), name='read'),
    path('update/<slug:slug>/', views.TodoUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', views.TodoDelete.as_view(), name='delete'),
]
