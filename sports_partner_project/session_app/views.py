from django.shortcuts import render
from session_app.models import Selection
from session_app.forms import SelectionForm


def index(request):
    return render(request, 'index.html', context={'index': index})


def contact(request):
	return render(request, 'contact.html', context={'contact': contact})


def categories(request):
	return render(request, 'categories.html', context={'categories': categories})


def selection_form(request):
	if request.method =='POST':
		Selection.objects.get_or_create(nbre_person_a=request.POST.get('nbre_person_a'), nbre_person_z=request.POST.get('nbre_person_z'), lieu=request.POST.get('lieu'), niveau=request.POST.get('niveau'), age_search=request.POST.get('age_search'), date=request.POST.get('date'))
		return redirect('success/')

	return render(request, 'selection_form.html', context={ 'selection_form': SelectionForm() })


def success(request):
	return render(request, 'success.html')

