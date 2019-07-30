from django.contrib import admin
from django.urls import path
import blogapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    path('new', blogapp.views.new, name='new'),
    path('signup/', blogapp.views.signup, name="signup"),
    path('login/', blogapp.views.login, name="login"),
    path('logout/', blogapp.views.logout, name="logout"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
