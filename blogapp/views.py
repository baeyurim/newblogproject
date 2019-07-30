from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import FileSystemStorage

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def new(request):
    if request.method == 'POST':     
        blog = Blog()
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)                   

            images = request.FILES['image']
            im = FileSystemStorage()
            blog.image = im.save(images.name, images)

            blog.date = timezone.datetime.now()
            blog.writer = request.user

            blog.save()

        return redirect('/blog/'+str(blog.id))
    
    else:
        form = BlogForm()
        return render(request,'new.html', {'form':form})

        
def signup(request):
    if request.method == 'POST':

        if request.POST['username'] == '' or request.POST['password'] == '':
            return render(request, 'signup.html', {'error':'아이디 비밀번호를 입력하세요'})
        
        if request.POST['password'] != request.POST['con_password']:
            return render(request, 'signup.html', {'error':'비밀번호 불일치'})

        try :
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'signup.html', {'error':'이미 존재하는 이름'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)

            return redirect('/')


    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(request, username = username, password = pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'아이디, 비밀번호 확인'})

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def detail(request, blog_id): 
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})
