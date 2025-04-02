from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def index(request):
    posts = Post.objects.order_by('-created_at')
    form = CommentForm()

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)

@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
        return redirect('posts:index')
    
@login_required    
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)

  # if post in user.like_posts.all(): 여기서는 related_name으로 접근
    if user in post.like_users.all(): # Post 클래스에 like_users 컬럼 만들었던걸로 접근
        post.like_users.remove(user)
    else:
        post.like_users.add(user)

    return redirect('posts:index')

def feed(request):
    followings = request.user.followings.all()

    posts = Post.objects.filter(user__in=followings) # 내가 팔로우 하는 사람들이 작성한 게시물들만!
    form = CommentForm()
    
    context = {
        'posts': posts,
        'form': form,
    }

    return render(request, 'index.html', context)

def like_async(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    # like랑 같은 구조로 행동을 하고 status만 추가해준 뒤
    if user in post.like_users.all():
        post.like_users.remove(user)
        status = False
    else:
        post.like_users.add(user)
        status = True

    context = {
        'post_id': id,
        'status': status,
        'count': len(post.like_users.all())
    }
    # json 데이터쪼가리(context)만 넘겨주기
    return JsonResponse(context)