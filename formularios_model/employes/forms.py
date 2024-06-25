from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = ['name', 'last_name', 'email']
        # fields = '__all__'
        # Si queremos todos menos alguno
        exclude = ('email',)
        # Añadir campo extra que no existe en el modelo
        # extra_fields = ['salari']
