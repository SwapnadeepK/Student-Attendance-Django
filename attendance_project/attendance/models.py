from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save

class Department(models.Model):
    dept_unique_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    total_teachers = models.IntegerField(default=0)
    subjects = models.ManyToManyField('Subject', related_name='departments')

    def __str__(self):
        return self.name

class Subject(models.Model):
    unique_subject_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    t_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    qualifications = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    usn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.IntegerField()
    student_class = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')])

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.date}"

@receiver(post_save, sender=User)
def add_superuser_to_teachers(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        teachers_group, created = Group.objects.get_or_create(name='Teachers')
        instance.groups.add(teachers_group)

@receiver(post_save, sender=User)
def add_new_user_to_students(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        students_group, created = Group.objects.get_or_create(name='Students')
        instance.groups.add(students_group)