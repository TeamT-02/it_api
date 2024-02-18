from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TeacherViewSet, UserViewSet, TeacherDetailView

router = SimpleRouter()

# router.register('', TeacherViewSet, basename='teacher')
router.register('', TeacherViewSet, basename='teacher')
# router.register('teacher/<int:pk/', TeacherDetailView, basename='teachera')
router.register('user', UserViewSet, basename='user')
# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('teacher/<int:pk/', TeacherDetailView.as_view(), name='teachera'),
    # path('teacher/<int:pk>/', teacher_detail, name='teacher'),
    # path('user', UserViewSet.as_view(), name='user1')
]
