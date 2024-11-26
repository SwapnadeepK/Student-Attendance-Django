from django.contrib import admin
from .models import Teacher, Department, Subject, Student, Attendance
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

class UserAdmin(BaseUserAdmin):
    fieldsets = list(BaseUserAdmin.fieldsets)
    # Check if 'groups' is already in the fieldsets
    if not any('groups' in fieldset[1].get('fields', []) for fieldset in fieldsets):
        fieldsets.append(
            (None, {'fields': ('groups',)}),
        )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Attendance)

