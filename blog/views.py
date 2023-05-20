from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# blog/

def blog(request):
	print('blog')
	return render(
		request,
		'blog/index.html'
	)




def exemplo(request):
	print('exemplo')
	return render(
		request,
		'blog/example.html'
	)