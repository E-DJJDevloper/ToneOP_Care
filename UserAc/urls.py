from django.urls import path
from .views import SignUpView, SignInView

# urlpatterns = [
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('signin/', SignInView.as_view(), name='signin'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUpView, name='user_list'),
    path('<int:pk>/', views.SignInView, name='user_detail'),
]