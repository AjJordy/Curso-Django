from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# blog/

def blog(request):
	print('blog')
	context = {
		'text': 'Olá blog',
		'title': 'Blog'
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