from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth
from django.shortcuts import redirect


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def logout(request):
    url_from = request.META['HTTP_REFERER']
    auth.logout(request)
    return redirect(url_from)