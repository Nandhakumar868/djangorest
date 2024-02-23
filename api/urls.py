from django.urls import path, include
from .views import PostRetrieveView

urlpatterns = [
    path('',PostRetrieveView.as_view(),name="home")
]
