import os
from django.shortcuts import render
from django.urls import resolve
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test, permission_required

# Create your views here.

def ArticleIndexView(request):
    context = {
        'pageTitle': 'Article Index',
        'title': 'Articles',
        'message': 'This is the index page for articles.'
    }

    print("there is a group : ", Group.objects.all())
    print("this user : ", request.user," is in groups : ", request.user.groups.all())


    
    return render(request, 'article/index.html', context)

@permission_required('article.delete_article')
def ArticleAddView(request):

    current_path = request.path
    path_parts = current_path.strip("/").split("/")
    path_link = []
    stringTemp = ""

    for i,item in enumerate(path_parts):    
        
        if i == 0:
            stringTemp += f"{item}:index"
            path_link.append(stringTemp)
            stringTemp = f"{item}:"
        else :
            stringTemp += f"{item}"
            path_link.append(stringTemp)


    path_name_link = zip(path_parts,path_link)
    
    context = {
        "pageTitle" : "add Article",
        "path_exploded" : path_name_link,
        # "path_exploded" : 
    }

    return render(request,'article/addArticle.html',context)