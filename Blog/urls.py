from django.urls import path

from .views import SignupView, Login, Profile, BlogCreation, BlogView, PostDelete, UpdatePost,  \
    Logout, UserDelete, UpdateUser,SinglePost

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('profile/<str:slug>/', Profile.as_view(), name='profile'),
    path('create-blog/', BlogCreation.as_view(), name='create_blog'),
    path('delete-post/<int:pk>/', PostDelete.as_view(), name='delete'),
    path('update/<str:slug>/', UpdatePost.as_view(), name='update'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user-delete/<str:slug>/', UserDelete.as_view(), name='user_delete'),
    path('update-user/<str:slug>/', UpdateUser.as_view(), name='updateUser'),
    path('single-post/<str:slug>/',SinglePost.as_view(),name='single_post')
]
