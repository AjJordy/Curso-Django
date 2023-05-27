from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from blog.data import posts
from typing import Any
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


def post(request: HttpRequest, post_id: int):
	print('post', post_id)
	found_post: dict[str, Any] | None = None
	for post in posts:
		if post['id'] == post_id:
			found_post = post
			break

	if found_post is None:
		raise Http404('Post não existe')

	context = {		
		'post': found_post,
		'title': found_post['title'] + ' - '
	}
	return render(
		request,
		'blog/post.html',
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