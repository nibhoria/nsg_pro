from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=50, primary_key = True)
    book_author = models.CharField(max_length=50)
    def __str__(self):
        return self.book_author
class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key = True)
    student_name =models.CharField(max_length=50)
    def __str__(self):
        return self.student_name

class Issued(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, unique= True, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(default=timezone.now)
    #return_date = models.DateTimeField(default=timezone.now())
    #fine = models.IntegerField(default = 'NULL' , null = True)
    def give_book(self):
        self.issued_date = timezone.now()
        self.save()
