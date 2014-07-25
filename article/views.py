from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from article.models import Article


def home(request):
    article = Article.objects.get(pk=2)
    return render_to_response('index.html',{'article':article}, context_instance=RequestContext(request))