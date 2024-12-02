from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Instructor, Course, Lesson
from .serializers import InstructorSerializer, CourseSerializer, LessonSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['specialization']
    search_fields = ['name', 'email']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['instructor', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    ordering_fields = ['start_date', 'end_date']


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['course', 'order']
    search_fields = ['title', 'content']
    ordering_fields = ['order']
