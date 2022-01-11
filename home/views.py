from django.contrib.auth import get_user_model
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Post
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
User = get_user_model()


@login_required
def profile_view(request, slug):
    p = Profile.objects.filter(slug=slug).first()
    u = p.user
    user_posts = Post.objects.filter(user_name=u)
    context = {
        'u': u,
        'post_count': user_posts.count
    }

    return render(request, "home/profile.html", context)

# register — Umożliwi to użytkownikom zarejestrowanie się w naszej witrynie. Wyrenderuje formularz rejestracyjny, który stworzyliśmy w pliku form.py.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'home/registration.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('my_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'home/edit_profile.html', context)

@login_required
def my_profile(request):
    p = request.user.profile
    you = p.user
    user_posts = Post.objects.filter(user_name=you)
    friends = p.friends.all()

    button_status = 'none'
    if p not in request.user.profile.friends.all():
        button_status = 'not_friend'

    context = {
        'u': you,
        'button_status': button_status,
        'friends_list': friends,
        'post_count': user_posts.count
    }

    return render(request, "home/profile.html", context)


def home(response):
    return render(response, "home/home.html", {})


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/login")
    form = RegisterForm()
    return render(request, "home/registration.html", {"form": form})


def login(request):
    return render(request, "home/login.html", {})
