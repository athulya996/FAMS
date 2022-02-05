from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from famsapp.forms import TeacherForm, StudentForm, AddGroup, AddProgram, AddResult
from famsapp.models import Teacher, Student, Group, Program, Result


def admin_home(request):
    return render(request, 'admin_home.html')


def home(request):
    return render(request, 'admintemp/home.html')


def add_teacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Invalid credentials")
            return redirect('add_teacher')
    # else:
    #     form = TeacherForm()
    return render(request, 'admintemp/add_teacher.html', {'form': form})


def view_teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'admintemp/view_teacher.html', {'teacher': teacher})


def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Invalid credentials")
            return redirect('add_student')
    # else:
    #     form = StudentForm()
    return render(request, 'admintemp/add_student.html', {'form': form})


def view_student(request):
    student = Student.objects.all()
    return render(request, 'admintemp/view_student.html', {'student': student})


def add_group(request):
    form = AddGroup()
    if request.method == 'POST':
        form = AddGroup(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Added Groups Successfully")
            return redirect('view_group')

    return render(request, 'admintemp/add_group.html', {'form': form})


def view_group(request):
    group = Group.objects.all()
    return render(request, 'admintemp/view_group.html', {'group': group})


def add_program(request):
    form = AddProgram()
    if request.method == 'POST':
        form = AddProgram(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Add program Successfully")
            return redirect('view_program')
    return render(request, 'admintemp/add_program.html', {'form': form})


def view_program(request):
    program = Program.objects.all()
    return render(request, 'admintemp/view_program.html', {'program': program})


def view_programreg(request):
    return render(request, 'admintemp/view_programreg.html')



def view_scoreboard(request):
    return render(request, 'admintemp/view_scoreboard.html')


def teacher_home(request):
    return render(request, 'teacher_home.html')


def home_teacher(request):
    return render(request, 'teacher_temp/home_teacher.html')


def student_view(request):
    student = Student.objects.all()
    return render(request, 'teacher_temp/student_view.html', {'student': student})


def program_view(request):
    program = Program.objects.all()
    return render(request, 'teacher_temp/program_view.html', {'program': program})


def add_result(request):
    form = AddResult()
    if request.method == 'POST':
        form = AddResult(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Add result successfully")
            return redirect('view_result')
    return render(request, 'teacher_temp/add_result.html', {'form': form})


def view_result(request):
    result = Result.objects.all()
    return render(request, 'teacher_temp/view_result.html', {'result': result})

def view_registration(request):
    return render(request, 'teacher_temp/view_registration.html')
