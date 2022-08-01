from django import forms
from app.models import Employee

# create a ModelForm
class EmployeeForm(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email'}))
	date_of_birth=forms.DateField(widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}))
	date_of_join=forms.DateField(widget=forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'}))

	designation=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Designation'}))
	reporting_manager=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Reporting Manager Name'}))
	class Meta:
		model = Employee
		fields = "__all__"

