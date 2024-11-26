from django import forms
from .models import Teacher, Department, Subject, Student, Attendance
from django.utils import timezone

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['t_id', 'name', 'department', 'qualifications']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_unique_id', 'name', 'total_teachers', 'subjects']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['unique_subject_id', 'name', 'department']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['usn', 'name', 'department', 'semester', 'student_class']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'subject', 'date', 'status']
        widgets = {
            'status': forms.RadioSelect(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')]),
            'date': forms.DateInput(attrs={'type': 'date', 'value': timezone.now().date()}),
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()
