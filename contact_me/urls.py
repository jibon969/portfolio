from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactList.as_view()),
    path('contact-detail/<int:pk>/', views.ContactDetail.as_view()),
]