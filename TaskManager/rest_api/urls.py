from django.urls import path, include
from rest_api.views import UserList, UserDetail, TaskViewSet, CommentViewSet, AttachmentViewSet, TaskListView, \
    TaskDetailView, TaskCreateView, CommentListView, CommentDeleteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'attachment', AttachmentViewSet, basename='attachment')

urlpatterns = [
    path('userlist/', UserList.as_view(), name='user-list'),
    path('userlist/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('', include(router.urls)),
    path('taskslist/', TaskListView.as_view(), name='task-list'),
    path('taskslist/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('taskslist/create', TaskCreateView.as_view(), name='task-create'),
    path('commentlist/', CommentListView.as_view(), name='comments-list'),
    path('commentlist/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete')
]

