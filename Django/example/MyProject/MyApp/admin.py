from django.contrib import admin
from .models import Student,Course,Department
from django import forms

class StudentAdmin(admin.ModelAdmin):
	pass

class CourseAdmin(admin.ModelAdmin):
	pass

class DepartmentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Department,DepartmentAdmin)

# Register your models here.
