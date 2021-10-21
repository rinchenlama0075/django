from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader

# Create your views here.


def indexView(request):
    # template = loader.get_template('help/index.html')
    return render(request, 'help/index.html', {'hello': 'hello'})
