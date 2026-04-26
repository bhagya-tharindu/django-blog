from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .forms import RegisterForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})