from django.urls import path
from .views import singnUpview
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', singnUpview.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
