from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('<int:id>/', views.post, name='post'),
	#path('register/', views.register, name='register'),
	path('login/', views.login_views, name='login'),
	path('logout/', views.logout_views, name='logout'),
]