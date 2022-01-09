from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_note', views.new_note, name = 'new'),
    path('note/<str:pk>', views.note_detail, name = 'note'),
    path('delete_note/<str:pk>', views.delete_note, name = 'delete'),
    path('search_result', views.search_page, name = 'search'),

]