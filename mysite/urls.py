
from django.urls import path, include
from django.contrib import admin
from blog import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post_new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
