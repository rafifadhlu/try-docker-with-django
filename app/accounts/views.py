from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .form import UploadAvaForm
from django.utils import timezone

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


# class loginView(TemplateView):
#     template_name = 'login/index.html'
#     context = {
#         'pageTitle': 'Login Page',
#         'title': 'Login to Your Account',
#         'message': 'Please enter your credentials to log in.'
#     }

#     def get(self, request):

#         return self.render_to_response(self.context)

class RegisterView(TemplateView):
    template_name = 'login/register.html'
    context = {
        'pageTitle': 'Register Page',
        'title': 'Create a New Account',
        'message': 'Fill in the form below to create a new account.'
    }

    def get(self, request):
        return self.render_to_response(self.context)
