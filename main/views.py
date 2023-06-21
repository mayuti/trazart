from django.shortcuts import render, redirect
from .models import Contact, Post
from .forms import PostForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def nav(request):
    return render(request, 'nav.html')

# Sección Blog
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'create_post.html', context)

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

# Fin Sección Blog

def about(request):
    return render(request, 'about.html')

# Sección Contacto
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comments = request.POST.get('comments')

        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, comments=comments)
        contact.save()

        return render(request, 'contactok.html')

    return render(request, 'contact.html')
# Fin Sección Contacto
