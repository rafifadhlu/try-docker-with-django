from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse

from django.contrib.auth.models import User
from .form import UploadAvaForm,RegisterUserForm
from django.utils import timezone
from .models import UserAva

# Create your views here.

def LoginDefView(request):
    context = {
        'pageTitle': 'Login Page',
    }

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username_input = request.POST['username']
        password_input = request.POST['password']

        user = authenticate(request, username=username_input, password=password_input)

        if user is not None:
            login(request, user)
        else:
            return redirect('account:register')
        
        return redirect('index')
    return render(request, 'login/index.html', context)

def LogoutView(request):

    if request.method == 'POST':
        logout(request)
        return redirect('index')

    context = {
        'pageTitle': 'Logout Page',
        'title': 'Logout from Your Account',
        'message': 'Are you sure you want to log out?'
    }
    return render(request, context)

@login_required
def TestPermissionView(request):
    context = {
        'pageTitle': 'Test Permission Page',
        'title': 'Test Your Permissions',
        'message': 'This page is for testing user permissions.'
    }

    return render(request, 'homeAdmin.html', context)

@login_required
def UploadAvatar(request):
    context = {
        'title' : "Upload File",
        'user' : request.user,
        'form' : UploadAvaForm
    }

    if request.method == 'POST':
        form = UploadAvaForm(request.POST, request.FILES)
        if form.is_valid():
            user_ava = form.save(commit=False)
            user_ava.id_user = request.user  # set the user manually
            user_ava.updated_at = timezone.now()
            user_ava.save()
            return redirect('index')
    else:
        form = UploadAvaForm()

    return render(request,'account/profile.html',context)


class RegisterView(CreateView):
    model = User
    template_name = 'login/register.html'
    form_class = RegisterUserForm
    
    def form_valid(self, form):
        # Modify the user object before saving
        user = form.save(commit=False)
        user.is_active = True
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('account:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Register Page'
        context['title'] = 'Create a New Account'
        context['message'] = 'Fill in the form below to create a new account.'
        
        return context