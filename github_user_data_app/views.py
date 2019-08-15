from django.shortcuts import HttpResponse, render
from django.shortcuts import render
from django.views.generic import View

import requests
import json
# Create your views here.

class IndexView(View):
    template_name = 'github_user_data_app/index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, context={'user_data': 'hello world'})


    def post(self, request, *args, **kwargs):
        github_url = "https://api.github.com/users/"+request.POST['user']

        req = requests.get(github_url)
        json_data = []
        json_data.append(json.loads(req.content))

        return render(request, self.template_name, context={})
