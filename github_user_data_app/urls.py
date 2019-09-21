from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('genPDF', GeneratePDF.as_view(), name="gen_pdf"),
]
