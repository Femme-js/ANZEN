from django.shortcuts import HttpResponse

def homePageView(request):
    return HttpResponse('Hello')


# Create your views here.
