from django.shortcuts import render, get_object_or_404, redirect
from app.models import Post, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def context_renderer(request):
    userSearchKeywork = request.GET.get('search')
    postSearch = []
    response = False
    if userSearchKeywork == None:
        pass
    else:
        postSearch = Post.objects.filter(Q(title__contains=userSearchKeywork) | Q(content__contains=userSearchKeywork))
        print(postSearch)
        if postSearch:
            pass
        else:
            response = True

    if postSearch:
        post  = postSearch
    else: 
        post = Post.objects.filter(approval=True, status='Publish')
    categories = Category.objects.all()
    postCat = []
    for c in categories:
        catCount = Post.objects.filter(category=c).count()
        postCat.append(catCount)
    postCategory = zip(categories, postCat)
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    recent_post = Post.objects.filter(approval=True, status='Publish').order_by('-created_at')[:3]
    
    return {
       'posts': posts,
        'postCategory': postCategory,
        'response': response,
        'recent_post': recent_post
    }