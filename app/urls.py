from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('pu_results/', views.pu_results, name="pu_results"),
    path('pu_listings/<int:lga_id>', views.pu_listings, name="pu_listings"),
    path('pu_lga_results/', views.pu_lga_results, name='pu_lga_results'),
    path('add_result/', views.add_result, name='add_result'),
]