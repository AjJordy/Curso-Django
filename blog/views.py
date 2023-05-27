from django.shortcuts import render
from django.http import HttpResponse
from blog.data import posts
# Create your views here.
# blog/

def blog(request):
	print('blog')
	context = {
		'text': 'Olá blog',
		'posts': posts
	}
	return render(
		request,
		'blog/index.html',
		context
	)




def exemplo(request):
	print('exemplo')
	context = {
		'text': 'Olá Exemplo',
		'title': 'Exemplo'
	}
	return render(
		request,
		'blog/example.html',
		context
	)