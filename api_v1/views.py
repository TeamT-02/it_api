from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView,RetrieveDestroyAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import TeacherSerializer, UserSerializer
from .models import Teacher
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


# class TeacherViewSet(ListCreateAPIView):

class TeacherViewSet(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(RetrieveAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = 'pk'


# def teacher_detail(request, pk):
#     teacher = get_object_or_404(Teacher, pk=pk)
#     return render(request, 'teacher.html', {'teacher': teacher})

# class TeacherViewSetDeatil(ModelViewSet):
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
