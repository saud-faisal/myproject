from django.shortcuts import render
from .models import SchoolEnrol
from .form import SchoolEnrolForm
from django.views.generics.list import ListView
# Create your views here.

def index(request):
	obj=SchoolEnrol.objects.all()
	return render(request, "myapp/start.html", {"obj":obj})
def AddNewStudent(request):
	if request. method==" POST":
		form=SchoolEnrolFrom(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/success/")
	else:
		form=SchoolEnrolForm()
		return render(request, "myapp/SchoolEnrolForm.HTML", {" form":form})
	
	
	