from django.urls import path
from .views import DrivesList, DriveDetail

urlpatterns = [
    path('drives/', DrivesList.as_view()),
    path('drive/<slug:pk>/', DriveDetail.as_view()),
]
