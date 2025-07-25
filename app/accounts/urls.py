from django.contrib import admin
from django.urls import path

from django.views.generic import RedirectView
from .views import RegisterView, LoginDefView, LogoutView,TestPermissionView,UploadAvatar

app_name = 'account'
urlpatterns = [
    path('', LoginDefView, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/',RedirectView.as_view(url='/account/'), name='login-redirect'),
    path('profile/',UploadAvatar, name='profile'),
    path('logout/', LogoutView, name='logout'),
    path('test-permission/', TestPermissionView, name='test-permission'),
]

# password admin
# id = rafi pass = saif123
# id = admin pass = Rafi1234
# id = septi pass = rafi1234
# id = saif pass = rafi1234

