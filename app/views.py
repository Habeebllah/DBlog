from django.shortcuts import render, get_object_or_404, redirect
from app.models import Post, Category, Comment
from app.form import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def Home(request):
    template_name = 'index.html'
    return render(request, template_name)

def BlogDetails(request, slug):
    template_name = 'details.html'
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            c = comment_form.save(commit=False)
            c.post = post
            c.save()
            return redirect(f'/detail/{post.slug}')

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, template_name, context)

def PostCategory(request, slug):
    template_name = 'category.html'
    PostCat = Post.objects.filter(category__slug = slug)
    context = {
        'postcat': PostCat,
    }
    return render(request, template_name, context)