from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import UrlForm
from .models import Link
from uuid import uuid4
from os import getcwd, getenv
from dotenv import load_dotenv

load_dotenv() 

LENGTH = 8
DOMAIN = getenv('DOMAIN')

def shorten(request):
	if request.method == 'POST':
		form = UrlForm(request.POST)
		url = request.POST.get('url', '')
		if(not url):
			return render(request, 'invalid.html')
		if(not url.startswith('http')):
			return render(request, 'invalid.html')

		lnks = Link.objects.all().filter(link=url)

		shortenedUrl = str(uuid4())[:LENGTH]
		lnk = Link(link=url, shortened=shortenedUrl, usages=0)
		lnk.save()
		shortenedUrl = DOMAIN + '/' + shortenedUrl
		if form.is_valid():
			context = { 
				'url' : shortenedUrl, 
				'orig' : url,
				'count' : len(lnks)
			}
			return render(request, 'shortened.html', context=context)

	form = UrlForm()
	return render(request, 'form.html', {'form': form})

def redirect_user(request, url):
	form = UrlForm()
	try:
		links = Link.objects.all().get(shortened=url)
	except ObjectDoesNotExist as e:
		print(e)
		return render(request, 'not-found.html')

	return redirect(links.link)