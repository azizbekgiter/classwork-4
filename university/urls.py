from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, CourseViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'instructors', InstructorViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]