from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
import requests

# Create your views here.





class MainView(View):
    def get(self, request, *args, **kwargs):
        PORT = request.META['SERVER_PORT'] 
        LOCAL_HOST_API = f'http://localhost:{PORT}/shorten/api/'
        response = requests.get(LOCAL_HOST_API)
        data = response.json()

        return render(request, 'shortener/index.html', {'data': data})


    def post(self, request, *args, **kwargs):
        PORT = request.META['SERVER_PORT'] 
        LOCAL_HOST_API = f'http://localhost:{PORT}/shorten/api/'
        long_url = request.POST['url']
        short_url = request.POST['short_url']
        if short_url == 'shorten':
            return redirect('/')
        if long_url:
            response = requests.post(LOCAL_HOST_API, 
                                     json={'long_url': long_url, 
                                           'short_url': short_url,
                                           'clicks': 0})

            if response.status_code == 201:
                return redirect('/')
            else:
                return redirect('/')
        else:
            return redirect('/')



class RedirectView(View):
    def get(self, request, *args, **kwargs):
        PORT = request.META['SERVER_PORT'] 
        LOCAL_HOST_API = f'http://localhost:{PORT}/shorten/api/'

        shorturl = kwargs['shorturl']
        response = requests.get(f'{LOCAL_HOST_API}{shorturl}')
        if response.status_code == 404:
            return redirect('/')
        data = response.json()

        requests.put(LOCAL_HOST_API + shorturl + '/',
                        json={
	                         'short_url': data['short_url'],
                             'long_url': data['long_url'],
                             "clicks" : data['clicks'] + 1
                             })


        return redirect(data['long_url'])
