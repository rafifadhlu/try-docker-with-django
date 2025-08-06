from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from accounts.models import UserAva # model UserAva
from utils import get_avatar_url
from django.conf import settings


def IndexView(request):
    template_name = None
    
    context = {
        'pageTitle': 'Home Page',
        'title': 'Welcome to My Docker-app',
        'message': 'This is a simple docker app with Django',
    }

    if request.user.is_authenticated:
        template_name = 'homeAuth.html'
        context['page'] = 'Authenticated'
        context['user'] = request.user.username

        try:
            user_ava = UserAva.objects.get(id_user=request.user)
        except UserAva.DoesNotExist:
            user_ava = None

        if request.user and user_ava:
            context['profilePicture'] = get_avatar_url(user_ava.ava,settings.SUPABASE_BUCKET)

    else:
        template_name = 'index.html'
        context['page'] = 'Home unauthenticated'
        context['user'] = None

    return render(request, template_name, context)