from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': "This is made by using django"}
    return render(request, 'Marc_Port_App/index.html', context=my_dict)
