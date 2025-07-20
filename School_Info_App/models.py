from django.db import models
from django.core.validators import RegexValidator

class Teacher_info_MODEL(models.Model) :
    teacher_id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=20)
    
    phone_validator = RegexValidator(r'^[0-9]{11}$', message="Phone number must be 11 digits.")

    teacher_phone = models.CharField(
        max_length=11,
        validators=[phone_validator],
        unique=True
    )
    teacher_email = models.EmailField(max_length=30, unique=True)
    teacher_address = models.TextField()
    teacher_subject = models.CharField(max_length=20)

    class Meta:
        db_table = 'teacher_info'
        verbose_name = 'Teacher Information'
        verbose_name_plural = 'Teachers Information'


class Student_info_MODEL(models.Model) :
    Student_id = models.AutoField(primary_key=True)
    Student_name = models.CharField(max_length=20)
    
    phone_validator = RegexValidator(r'^[0-9]{11}$', message="Phone number must be 11 digits.")

    Student_phone = models.CharField(
        max_length=11,
        validators=[phone_validator],
        unique=True
    )
    Student_email = models.EmailField(max_length=30, unique=True)
    Student_address = models.TextField()
    Section = models.CharField(max_length=1)

    class Meta:
        db_table = 'student_info'
        verbose_name = 'Student Information'
        verbose_name_plural = 'Students Information'