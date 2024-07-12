from django.urls import path
from .views import(
			 HeartRateAPIView, 
			 HeartRateDetailAPIView,
			 RegisterAPIView
	)

urlpatterns = [
    path('list', HeartRateAPIView.as_view(), name='heart_rate_api_view'),
    path('register', RegisterAPIView.as_view(), name='register_api_view'),
    path('<int:pk>/', HeartRateDetailAPIView.as_view(), name='heart_rate_detail'),

]