from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Student
from .models import Issued
#from .models import Returned

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Issued)
#admin.site.register(Returned)
