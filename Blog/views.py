from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post
from .forms import LoginForm, SignUpForm, BlogForm
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django_email_verification import sendConfirm

User = get_user_model()


class BlogView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'blogs'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = '/'


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = '/login'

    def form_valid(self, form):
        print("form valid")
        # sendConfirm(self.object.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("invalid")
        return super().form_invalid(form)


class SinglePost(DetailView):
    context_object_name = 'blog'
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/single_post.html'


@method_decorator(login_required(), name='dispatch')
class UpdatePost(UpdateView):
    form_class = BlogForm
    slug_url_kwarg = 'slug'
    model = Post
    template_name = 'blog/update_blog.html'
    success_url = '/'


@method_decorator(login_required(), name='dispatch')
class Profile(DetailView):
    model = User
    context_object_name = 'profile'
    slug_url_kwarg = 'slug'
    template_name = 'blog/profile.html'


@method_decorator(login_required(), name='dispatch')
class BlogCreation(CreateView):
    form_class = BlogForm
    model = Post
    template_name = 'blog/create_blog.html'
    slug_url_kwarg = 'slug'
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required(), name='dispatch')
class UpdateUser(UpdateView):
    model = User
    form_class = SignUpForm
    slug_url_kwarg = 'slug'
    template_name = 'registration/update_user.html'
    success_url = '/'


class Logout(LogoutView):
    template_name = 'blog/index.html'


@method_decorator(login_required(), name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@method_decorator(login_required(), name='dispatch')
class UserDelete(DeleteView):
    model = User
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
