from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('doing/', views.doing, name='doing'),
    path('done/', views.done, name='done'),
    path('delete/', views.delete, name='delete')
]
