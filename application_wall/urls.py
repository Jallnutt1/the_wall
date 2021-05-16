from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('messagePost', views.messagePost),
    path('commentPost/<int:id>', views.commentPost),
    path('deleteComment/<int:id>',views.deleteComment),
    path('deleteMessage/<int:id>',views.deleteMessage)
]

