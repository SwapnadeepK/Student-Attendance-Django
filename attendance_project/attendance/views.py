from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Teacher, Department, Subject, Student, Attendance
from .forms import TeacherForm, DepartmentForm, SubjectForm, StudentForm, AttendanceForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone

def is_teacher(user):
    return user.groups.filter(name='Teachers').exists()

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'attendance/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'attendance/home.html')

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'attendance/teacher_list.html', {'teachers': teachers})

@login_required
@user_passes_test(is_teacher)
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'attendance/add_teacher.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'attendance/edit_teacher.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'attendance/delete_teacher.html', {'teacher': teacher})

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'attendance/department_list.html', {'departments': departments})

@login_required
@user_passes_test(is_teacher)
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'attendance/add_department.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'attendance/edit_department.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'attendance/delete_department.html', {'department': department})

@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'attendance/subject_list.html', {'subjects': subjects})

@login_required
@user_passes_test(is_teacher)
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'attendance/add_subject.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'attendance/edit_subject.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'attendance/delete_subject.html', {'subject': subject})

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'attendance/student_list.html', {'students': students})

@login_required
@user_passes_test(is_teacher)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'attendance/add_student.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'attendance/edit_student.html', {'form': form})

@login_required
@user_passes_test(is_teacher)
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'attendance/delete_student.html', {'student': student})

@login_required
@user_passes_test(is_teacher)
def attendance_form(request):
    students = Student.objects.all()
    subjects = Subject.objects.all()

    if request.method == 'POST':
        subject_id = request.POST['subject']
        subject = Subject.objects.get(id=subject_id)
        date = request.POST['date']

        for student in students:
            status = request.POST.get(f'status_{student.id}')
            if status:
                attendance, created = Attendance.objects.get_or_create(
                    student=student,
                    subject=subject,
                    date=date,
                    defaults={'status': status}
                )
                if not created:
                    attendance.status = status
                    attendance.save()

        return redirect('attendance_list')

    context = {
        'students': students,
        'subjects': subjects,
        'date': timezone.now().date().strftime('%Y-%m-%d'),
    }
    return render(request, 'attendance/attendance_form.html', context)

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})
