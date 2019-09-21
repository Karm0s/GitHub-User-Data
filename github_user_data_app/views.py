from django.shortcuts import HttpResponse, render
from django.shortcuts import render
from django.views.generic import View
from django.utils import translation

import requests
import json

from .utils import render_to_pdf
# Create your views here.

user_data = {}


class IndexView(View):
    template_name = 'github_user_data_app/index.html'

    def get(self, request, *args, **kwargs):

        translation.activate('en')
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


            if "checkbox-pdf" in request.POST:
                context['download_pdf'] = 'YES'
                self.request.session['user_data'] = context

        elif user_data.status_code == 404:
            context = {'status_code': 'ERR_NF', 'user_name': request.POST['user']}
        

        return render(request, self.template_name, context=context)

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf("github_user_data_app/pdf/user_data.html", self.request.session.get('user_data'))
        return pdf
