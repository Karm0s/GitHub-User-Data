from django.shortcuts import HttpResponse, render
from django.shortcuts import render
from django.views.generic import View

import requests
import json
# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get(self, request):

        res = requests.get('https://api.github.com/users/Karm0s')


        return HttpResponse(res)
