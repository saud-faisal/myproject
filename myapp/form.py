from django import forms
from .models import SchoolEnrol

class SchoolEnrolForm(forms.ModelForm):
	class Meta:
		model=SchoolEnrol
		fields=["first_name","father_name","DOB"]