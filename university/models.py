from django.db import models
from django.core.validators import EmailValidator, validate_email
from django.core.exceptions import ValidationError

class Instructor(models.Model):
    """O'qituvchi modeli"""
    name = models.CharField(max_length=200, verbose_name='Ismi')
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        verbose_name='Elektron pochta'
    )
    specialization = models.CharField(
        max_length=200,
        verbose_name='Mutaxassisligi'
    )

    def clean(self):
        """Email validatsiyasi"""
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError({'email': 'Noto\'g\'ri email formati'})

    def __str__(self):
        return f"{self.name} ({self.specialization})"

class Course(models.Model):
    """Kurs modeli"""
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsif')
    start_date = models.DateField(verbose_name='Boshlanish sanasi')
    end_date = models.DateField(verbose_name='Tugash sanasi')
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='O\'qituvchi'
    )

    def clean(self):
        """Sana validatsiyasi"""
        if self.start_date >= self.end_date:
            raise ValidationError({
                'end_date': 'Tugash sanasi boshlanish sanasidan keyinroq bo\'lishi kerak'
            })

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Dars modeli"""
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    content = models.TextField(verbose_name='Mazmuni')
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Kurs'
    )
    order = models.PositiveIntegerField(verbose_name='Tartib raqami')

    class Meta:
        unique_together = ['course', 'order']
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title} (Dars {self.order})"