from django.shortcuts import HttpResponse, render
from django.shortcuts import render
from django.views.generic import View

import requests
import json
# Create your views here.

class IndexView(View):
    template_name = 'github_user_data_app/index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        github_api_user_url = "https://api.github.com/users/"+request.POST['user']
        github_api_user_repos_url = github_api_user_url + "/repos"


        user_data = requests.get(github_api_user_url)


        if user_data.status_code == 200:
            user_json_data = json.loads(user_data.content)

            repos_data = requests.get(github_api_user_repos_url)
            repos_json_data = json.loads(repos_data.content)
            context = {'status_code': 'OK', 'user_data': user_json_data, 'repos_data': repos_json_data}
        elif user_data.status_code == 404:
            context = {'status_code': 'ERR_NF', 'user_name': request.POST['user']}

        return render(request, self.template_name, context=context)
