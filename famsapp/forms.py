from django import forms

from famsapp.models import Teacher, Student, Group, Program, Result


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'email', 'contact_no', 'department', 'group')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'contact_no', 'roll_no', 'semester', 'department', 'group')


class AddGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('group_no', 'group_name', 'group_teacher')


class AddProgram(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'rule', 'type', 'limitations_of_participations')


class AddResult(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('program', 'student', 'mark', 'group')