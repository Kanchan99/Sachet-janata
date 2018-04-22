from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView,CreateView
#from django.views.generic import TemplateView
# Create your views here.
from .models import City,Events
from django.http import HttpResponseRedirect

def home(request):
	return render(request,template_name='home.html')
def contact(request):
    return render(request,template_name='contact.html')
def aboutus(request):
    return render(request,template_name='aboutus.html')
def progressreport(request):
	return render(request,template_name='visualization.html')
def search(request):
	srch= request.GET.get('srh')
	if 'srh' in request.GET:
		srch = request.GET.get('srh').strip()

		# print(srch)

		if srch:
			match=City.objects.filter(Q(name__icontains=srch) |
									 Q(state__icontains=srch) |
									 Q(governor__icontains=srch)
			   						)
			if match:
				return render(request,'home.html',{'sr':match})

			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('/search/')
	return render(request,'home.html')



class EventListView(ListView):
	model=Events 
	template_name='eventlist.html'
	fields="__all__"
	context_object_name='events'

class EventCreateView(CreateView):
	model=Events
	template_name='eventcreate.html'
	fields="__all__"
	success_url="/"