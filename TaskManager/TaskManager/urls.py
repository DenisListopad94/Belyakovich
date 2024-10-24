from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views
from base.views import TasksView, UsersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tasks/', TasksView.as_view(), name='tasks'),
    path('users/', UsersView.as_view(), name='users'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('homework/', views.show_tasks, name='show_tasks'),
    path('new_task/', views.new_task, name='new_task'),
    path('new_com/', views.add_comment, name='add_comment'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
