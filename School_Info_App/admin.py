from django.contrib import admin
from .models import Teacher_info_MODEL
from .models import Student_info_MODEL

admin.site.register(Teacher_info_MODEL)
admin.site.register(Student_info_MODEL)

