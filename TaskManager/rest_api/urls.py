from django.urls import path, include
from rest_api.views import UserList, UserDetail, TaskViewSet, CommentViewSet, AttachmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'attachment', AttachmentViewSet, basename='attachment')

urlpatterns = [
    path('userlist/', UserList.as_view(), name='user-list'),
    path('userlist/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('', include(router.urls)),
]

