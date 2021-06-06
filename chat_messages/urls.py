from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from chat_messages import views

urlpatterns = [
    path('', views.MessageList.as_view()),
    path('<int:pk>/', views.MessageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
