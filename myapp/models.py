from django.db import models

# Create your models here.
class SchoolEnrol(models.Model):
	classOpted=(("5", "5"),
	(" 6", "6"),
	(" 7", "7"),
	(" 8", "8"),
	(" 9", "9"),
	(" 10", "10"),
	)
	first_name=models.CharField(max_length=100)
	father_name=models.CharField(max_length=100)
	DOB=models.DateTimeField()
	addres=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	pin=models.IntegerField()
	phone_no=models.IntegerField(unique=True)
	email=models.EmailField(unique=True)
	class_opted=models.CharField(max_length=100,choices=classOpted)
	marks=models.CharField(max_length=100)
	date_of_joining=models.DateTimeField()
	
	
	
	
	
	