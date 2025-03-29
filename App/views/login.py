from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')  
    
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')