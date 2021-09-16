from django.urls import path

from .views import home_view, account, rating, about_us, Pushkin, Pushkin2, int_ideas

urlpatterns = [
    path('account/', account, name = "account"),
    path('about_us/', about_us, name = "about_us"),
    path('int_ideas_for_date', int_ideas, name = "int_ideas"),
    path('<str:something>/', rating, name = "rating"),
    path('Pushkin_card', Pushkin, name = "Pushkin"),
    path('Pushkin_card/<str:event>', Pushkin2, name = "Pushkin2"),
    path('', home_view, name = "home_page")
]


