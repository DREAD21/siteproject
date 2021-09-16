from django.urls import path

from .views import SignUpView, logout

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout', logout, name='logout')
]