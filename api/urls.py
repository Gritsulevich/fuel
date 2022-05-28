from django.urls import include, path
from . import views

urlpatterns = [
    path('company/<str:pk>/', views.Auth_all.as_view()),
    path('company/user/<str:pk>/', views.User.as_view()),
    path('company/create/<str:token>/', views.CompanyCreate.as_view()),
    path('company/updata/<int:pk>/<str:token>/', views.CompanyDetail.as_view()),
    
    path('station/create/', views.StationCreate.as_view()),
    path('station/', views.StationList.as_view()),
    path('station/<int:pk>/', views.StationDetail.as_view()),
    path('fuel/create/', views.FuelinfoCreate.as_view()),
    path('fuel/', views.FuelinfoList.as_view()),
    path('fuel/<int:pk>/', views.FuelinfoDetail.as_view()),
    
]
