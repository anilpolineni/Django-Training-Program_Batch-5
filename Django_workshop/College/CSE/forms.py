from django.forms import ModelForm
from .models import Faculty


class FacultyRegisterForm(ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        # fields = ['email','name']