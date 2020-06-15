from django.urls import path
from Breed import views

urlpatterns = [
    path('breeds/', views.BreedList.as_view()),
    path('breeds/<int:pk>/', views.BreedDetail.as_view()),
    path('breeds/<int:pk>/random', views.BreedDetailRandom.as_view()),
]