from django import forms
from .models import Issued
class ReturnForm(forms.ModelForm):

	class Meta:
		model = Issued
		fields = ('student_id', 'book_id',)