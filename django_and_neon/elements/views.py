from django.shortcuts import render

# Create your views here.

from .models import Element
def elements_list(request):
    elements = Element.objects.all() 
    return render(request, 'elements_list.html', {'elements': elements})
