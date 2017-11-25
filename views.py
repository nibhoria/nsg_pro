from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Issued
from .forms import ReturnForm
from django.http import HttpResponse

# Create your views here.

def issued_list(request):
    all_books = Issued.objects.order_by('student_id')
    return render(request,'books/issued_list.html', {'all_books':all_books})

def return_form(request):
	return render(request,'books/return_form.html',{})

def delet(request,x): 
	if Issued.objects.filter(book_id=x):
		Issued.objects.filter(book_id=x).delete()
		#Issued.objects.all().delete()
		return HttpResponse("The book is returned")
	else:
		return HttpResponse("No such book is issued")
