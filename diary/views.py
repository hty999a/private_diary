#####              #####
    #2つの追加or変更#
#####              #####
from django.shortcuts import render
from django.views import generic ###1 追加###

class IndexView(generic.TemplateView):  ###2 追加###
    template_name = "index.html"
# Create your views here.
