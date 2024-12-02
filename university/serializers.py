from rest_framework import serializers
from .models import Instructor, Course, Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email', 'specialization']

    def validate_email(self, value):

        return value


class LessonSerializer(serializers.ModelSerializer):


    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'course', 'order']

    def validate_order(self, value):

        if value <= 0:
            raise serializers.ValidationError("Tartib raqami musbat bo'lishi kerak")
        return value


class CourseSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(many=True, read_only=True)
    instructor_details = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'start_date',
                  'end_date', 'instructor', 'instructor_details',
                  'lessons']
        read_only_fields = ['instructor_details']

    def validate(self, data):

        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date and start_date >= end_date:
            raise serializers.ValidationError({
                'end_date': 'Tugash sanasi boshlanish sanasidan keyinroq bo\'lishi kerak'
            })
        return data

    def get_instructor_details(self, obj):

        return {
            'name': obj.instructor.name,
            'email': obj.instructor.email,
            'specialization': obj.instructor.specialization
        }