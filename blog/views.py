from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# blog/

def blog(request):
	print('blog')
	return HttpResponse('blog do app')


def exemplo(request):
	print('exemplo')
	return HttpResponse('exemplo do app')