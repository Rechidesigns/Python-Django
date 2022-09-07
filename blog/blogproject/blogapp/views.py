from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage

# from django.



def home_page(request):
    post_list = Post.objects.filter(status="published")
    
    paginator = Paginator(post_list, 3)
    
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
        
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    
    progress = (posts.number/paginator.num_pages) * 100
    
    return render(request, 
                  "index.html",
                  {'posts': posts,
                   "page":page,
                   "progress": int(progress)})
    

def post_detail(request, year, month, day, slug):
    new_comment = False
    post = get_object_or_404(Post, publish__year=year, 
                             publish__month=month,
                             publish__day=day, 
                             slug=slug)
    
    all_comments = post.comments.all()
    prev_post_list = Post.objects.filter(publish__lt=post.publish)
    
    if prev_post_list.count() == 0:
        prev_post = None
    else:
        prev_post = prev_post_list.first()
        
    next_post_list = Post.objects.filter(publish__gt=post.publish)
    if next_post_list.count() == 0:
        next_post = None
    else:
        next_post = next_post_list.last()
        
        
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Comment.objects.create(name=name, email=email, message=message, blog_post=post)
        new_comment = True
    
    return render(request,
                'single.html',
                {'post': post,
                 'prev_post':prev_post,
                 'next_post':next_post,
                 "new_comment":new_comment,
                 "all_comments":all_comments})
    